from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.forms.models import modelformset_factory
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

from .forms import DropForm
from .models import Drop



@login_required
def drop_list_view(request, id=None):
    qs = Drop.objects.filter(user=request.user)
    context = {
        "object_list": qs
    }
    return render(request, "drops/list.html", context)

@login_required
def drop_detail_view(request, id=None):
    hx_url = reverse("drops:hx-detail", kwargs={"id": id})
    context = {
        "hx_url": hx_url
    }
    return render(request, "drops/detail.html", context)

@login_required
def drop_delete_view(request, id=None):
    try:
        obj = Drop.objects.get(id=id, user=request.user)
    except:
        obj = None
    if obj is None:
        if request.htmx:
            return HttpResponse("Not Found")
        raise Http404
    if request.method == "POST":
        obj.delete()
        success_url = reverse('drops:list')
        if request.htmx:
            headers = {
                'HX-Redirect': success_url
            }
            return HttpResponse("Success", headers=headers)
        return redirect(success_url)
    context = {
        "object": obj
    }
    return render(request, "drops/single.html", context)

@login_required
def drop_create_view(request):
    form = DropForm(request.POST or None, request.FILES or None)
    context = {
        "form": form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        if request.htmx:
            headers = {
                "HX-Redirect": obj.get_absolute_url()
            }
            return HttpResponse("Created", headers=headers)
        return redirect(obj.get_absolute_url())
    return render(request, "drops/create-update.html", context=context)

@login_required
def drop_update_view(request, id=None):
    obj = get_object_or_404(Drop, id=id, user=request.user)
    form = DropForm(request.POST or None, request.FILES or None, instance=obj)
    context = {
        "form": form,
        "object": obj,
    }
    if form.is_valid():
        form.save()
        context['message'] = 'Data saved.'
    if request.htmx:
        return render(request, "nftcollections/partials/forms.html", context)
    return render(request, "nftcollections/create-update.html", context)

@login_required
def drop_detail_hx_view(request, id=None):
    try:
        obj = Drop.objects.get(id=id, user=request.user)
    except:
        obj = None
    if obj is  None:
        return HttpResponse("Not found.")
    context = {
        "object": obj
    }
    return render(request, "drops/partials/detail.html", context)

def drop_single_view(request, slug=None):
    drop_obj = None
    if slug is not None:
        try:
            drop_obj = Drop.objects.get(slug=slug)
        except Drop.DoesNotExist:
            raise Http404
        except Drop.MultipleObjectsReturned:
            drop_obj = Drop.objects.filter(slug=slug).first()
        except:
            raise Http404
    context = {
        "object": drop_obj,
    }
    return render(request, "drops/single.html", context=context)

def schedule_view(request, *args, **kwargs):
    drop_queryset = Drop.objects.all()
    total_of_drops = Drop.objects.all().count()

    p = Paginator(drop_queryset, 5)
    page = request.GET.get('page')
    drops = p.get_page(page)
    nums = "a" * drops.paginator.num_pages

    context = {
        "object_list": drop_queryset,
        "total_of_drops": total_of_drops,
        "drops": drops,
        "nums": nums
    }
    return render(request, "schedule-view.html", context=context)

def drop_search_view(request):
    query = request.GET.get('q')
    qs = Drop.objects.search(query=query)
    context = {
        "object_list": qs
    }
    return render(request, "drops/drop-search.html", context=context)
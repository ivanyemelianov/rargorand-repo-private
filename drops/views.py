from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, redirect

from .forms import DropForm
from .models import Drop

def drop_search_view(request):
    query = request.GET.get('q')
    qs = Drop.objects.all()
    if query is not None:
        lookups = Q(title__icontains=query) | Q(description__icontains=query)
        qs = Drop.objects.filter(lookups)
    context = {
        "object_list": qs
    }
    return render(request, "drops/drop-search.html", context=context)

@login_required
def drop_create_view(request):
    form = DropForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        drop_obj = form.save()
        context['form'] = DropForm()
        return redirect(drop_obj.get_absolute_url()) 
    return render(request, "drops/drop-create.html", context=context)


def drop_detail_view(request, slug=None):
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
    return render(request, "drops/drop-detail.html", context=context)

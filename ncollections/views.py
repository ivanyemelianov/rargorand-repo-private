from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.forms.models import modelformset_factory
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.core.paginator import Paginator

from .models import Ncollection, Nnft, Nattribute
from .forms import NcollectionForm, NnftForm, NattributeForm

@login_required
def collection_list_view(request):
    qs = Ncollection.objects.filter(user=request.user)
    context = {
        "object_list": qs
    }
    return render(request, "ncollections/list.html", context)

@login_required
def collection_detail_view(request, id=None):
    obj = get_object_or_404(Ncollection, id=id, user=request.user)
    context = {
        "object": obj
    }
    return render(request, "ncollections/detail.html", context)

@login_required
def collection_delete_view(request, id=None):
    obj = get_object_or_404(Ncollection, id=id, user=request.user)
    if request.method == "POST":
        obj.delete()
        success_url = reverse('ncollections:list')
        return redirect(success_url)
    context = {
        "object": obj
    }
    return render(request, "ncollections/delete.html", context)

@login_required
def collection_create_view(request):
    form = NcollectionForm(request.POST or None, request.FILES or None)
    context = {
        "form": form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect(obj.get_absolute_url())
    return render(request, "ncollections/create-update.html", context)

@login_required
def collection_update_view(request, id=None):
    obj = get_object_or_404(Ncollection, id=id, user=request.user)
    form = NcollectionForm(request.POST or None, request.FILES or None, instance=obj)
    context = {
        "form": form,
        "object": obj
    }
    if form.is_valid():
        form.save()
        context['message'] = 'Data saved.'
    return render(request, "ncollections/create-update.html", context)

@login_required
def nnft_detail_view(request, parent_id=None, id=None):
    #obj = get_object_or_404(Nnft, collection=parent_id, id=id, user=request.user) # most likely not user, but collection
    hx_url = reverse("ncollections:hx-nft-detail", kwargs={"parent_id": parent_id, "id": id })
    context = {
        "hx_url": hx_url
    }
    return render(request, "ncollections/nft-detail.html", context)

@login_required
def nnft_delete_view(request, parent_id=None, id=None):
    try:
        obj = Nnft.objects.get(collection=parent_id, id=id, user=request.user)
        #obj = get_object_or_404(Nnft, collection=parent_id, id=id, user=request.user)
    except:
        obj = None
    if obj is None:
        if request.htmx:
            return HttpResponse("Not Found")
        raise Http404
    if request.method == "POST":
        obj.delete()
        success_url = reverse('ncollections:detail', kwargs={"id": parent_id})
        if request.htmx:
            headers = {
                'HX-Redirect': success_url
            }
            return HttpResponse("Success", headers=headers)
        return redirect(success_url)
    context = {
        "object": obj
    }
    return render(request, "ncollections/delete-nft.html", context)

@login_required
def nnft_detail_hx_view(request, parent_id=None, id=None):
    if not request.htmx:
        raise Http404
    try:
        obj = Nnft.objects.get(collection=parent_id, id=id, user=request.user)
    except:
        obj = None
    if obj is None:
        return HttpResponse("Not found.")
    context = {
        "object": obj
    }
    return render(request, "ncollections/partials/nft-detail.html", context)

@login_required
def nnft_create_view(request, parent_id=None):
    parent_obj = get_object_or_404(Ncollection, id=parent_id, user=request.user)
    form = NnftForm(request.POST or None, request.FILES or None, initial={'collection': parent_obj.id})
    context = {
        "form": form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect(obj.get_hx_url())
    return render(request, "ncollections/nft-create-update.html", context)


@login_required
def nnft_update_view(request, parent_id=None, id=None):
    obj = get_object_or_404(Nnft, collection=parent_id, id=id, user=request.user)
    form = NnftForm(request.POST or None, request.FILES or None, instance=obj)
    new_attribute_url = reverse("ncollections:hx-attribute-create", kwargs={"parent_id": obj.id})
    context = {
        "form": form,
        "object": obj,
        "new_attribute_url": new_attribute_url 
    }
    if form.is_valid():
        form.save()
        context['message'] = 'Data saved.'
    if request.htmx:
        return render(request, "ncollections/partials/forms.html", context)
    return render(request, "ncollections/nft-create-update.html", context)  


@login_required
def nnft_attribute_delete_view(request, collection_id=None, parent_id=None, id=None):
    try:
        obj = Nattribute.objects.get(nft__id=parent_id, id=id, nft__user=request.user)
        #obj = get_object_or_404(Nnft, collection=parent_id, id=id, user=request.user)
    except:
        obj = None
    if obj is None:
        if request.htmx:
            return HttpResponse("Not Found")
        raise Http404
    if request.method == "POST":
        obj.delete()
        kwargs = {
            "parent_id": collection_id,
            "id": parent_id   
        }
        success_url = reverse('ncollections:nft-detail', kwargs=kwargs)
        if request.htmx:
            headers = {
                'HX-Redirect': success_url
            }
            return HttpResponse("Success", headers=headers)
        return redirect(success_url)
    context = {
        "object": obj
    }
    return render(request, "ncollections/delete-nft.html", context)


@login_required
def nnft_attribute_update_hx_view(request, parent_id=None, id=None):
    if not request.htmx:
       raise Http404
    try:
        parent_obj = Nnft.objects.get(id=parent_id, user=request.user)
    except:
        parent_obj = None
    if parent_obj is None:
        return HttpResponse("Not found.")
    instance = None
    if id is not None:  
        try:
            instance = Nattribute.objects.get(nft=parent_obj, id=id)
        except:
            instance = None
    form = NattributeForm(request.POST or None, instance=instance)
    url = reverse("ncollections:hx-attribute-create", kwargs={"parent_id": parent_obj.id})
    if instance:
        url = instance.get_hx_edit_url()
    context = {
        "url": url,
        "form": form,
        "object": instance
    }
    if form.is_valid():
        new_obj = form.save(commit=False)
        if instance is None:
            new_obj.nft = parent_obj
        new_obj.save()
        context['object'] = new_obj
        return render(request, "ncollections/partials/attribute-inline.html", context)
    return render(request, "ncollections/partials/attribute-form.html", context)

def ncollection_single_view(request, slug=None, id=None):
    collection_obj = None
    list_of_nfts = Nnft.objects.filter(collection=id) #filter(collection__name=slug).all()
    total_of_nfts = len(list_of_nfts)
   
    if slug is not None:
        try:
            collection_obj = Ncollection.objects.get(slug=slug)
        except Ncollection.DoesNotExist:
            raise Http404
        except Ncollection.MultipleObjectsReturned:
            collection_obj = Ncollection.objects.filter(slug=slug).first()
        except:
            raise Http404
    
    p = Paginator(list_of_nfts, 24)
    page = request.GET.get('page')
    nfts = p.get_page(page)
    nums = "a" * nfts.paginator.num_pages

    context = {
        "object": collection_obj,
        "total_of_nfts": total_of_nfts,
        "nfts": nfts,
        "nums": nums
    }
    return render(request, "ncollections/single.html", context=context)

def g_collection_list_view(request):
    collection_queryset = Ncollection.objects.all()
    context = {
        "object_list": collection_queryset,
    }
    return render(request, "ncollections/collection-list.html", context=context)
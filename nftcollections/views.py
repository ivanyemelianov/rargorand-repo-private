from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory
from django.shortcuts import redirect, render, get_object_or_404

from .forms import NftCollectionForm, NftForm
from .models import NftCollection, Nft
# Create your views here.

@login_required
def nftcollection_list_view(request, id=None):
    qs = NftCollection.objects.filter(user=request.user)
    context = {
        "object_list": qs
    }
    return render(request, "nftcollections/list.html", context)

@login_required
def nftcollection_detail_view(request, id=None):
    obj = get_object_or_404(NftCollection, id=id, user=request.user)
    context = {
        "object": obj
    }
    return render(request, "nftcollections/detail.html", context)

@login_required
def nftcollection_create_view(request):
    form = NftCollectionForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect(obj.get_absolute_url())
    return render(request, "nftcollections/create-update.html", context)

@login_required
def nftcollection_update_view(request, id=None):
    obj = get_object_or_404(NftCollection, id=id, user=request.user)
    form = NftCollectionForm(request.POST or None, instance=obj)
    # Formset = modelformset_factory(Model, form=ModelForm, extra=0)
    NftFormset = modelformset_factory(Nft, form=NftForm, extra=0)
    qs = obj.nft_set.all() # []
    formset = NftFormset(request.POST or None, queryset=qs)
    context = {
        "form": form,
        "formset": formset,
        "object": obj
    }
    if all([form.is_valid(), formset.is_valid()]):
        parent = form.save(commit=False)
        parent.save()
        # formset.save()
        for form in formset:
            child = form.save(commit=False)
            if child.nftcollection is None:
                child.nftcollection = parent
            child.save()
        context['message'] = 'Data saved.'
    return render(request, "nftcollections/create-update.html", context)

def all_collections_view(request):
    drop_queryset = NftCollection.objects.all()
    context = {
        "object_list": drop_queryset,
    }
    return render(request, "collections-view.html", context=context)
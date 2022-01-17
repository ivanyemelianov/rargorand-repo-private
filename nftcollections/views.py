from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from .forms import NftCollectionForm
from .models import NftCollection
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
    context = {
        "form": form,
        "object": obj
    }
    if form.is_valid():
        form.save()
        context['message'] = "Data saved."
    return render(request, "nftcollections/create-update.html", context)
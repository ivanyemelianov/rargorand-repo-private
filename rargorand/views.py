import random
from django.shortcuts import redirect, render, get_object_or_404

from drops.models import Drop


def home_view(request, *args, **kwargs):
    drop_queryset = Drop.objects.all()
    context = {
        "object_list": drop_queryset,
    }
    return render(request, "home-view.html", context=context)
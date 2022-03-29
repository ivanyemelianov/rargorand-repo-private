import random
from django.shortcuts import redirect, render, get_object_or_404

from drops.models import Drop
from ncollections.models import Ncollection


def home_view(request, *args, **kwargs):
    drop_queryset = Drop.objects.all()
    last_six_drops_q = Drop.objects.filter().order_by('-id')[:6]
    featured_q = Ncollection.objects.filter(featured=True)
    last_eight_q = Ncollection.objects.filter().order_by('-id')[:6]
    featured_drop_q = Drop.objects.filter(featured=True)
    ma_drop_q = Drop.objects.filter(mostanticipated=True)
    ff_drop_q = Drop.objects.filter(futurefavourite=True)
    context = {
        "object_list": drop_queryset,
        "upcomming_drops": last_six_drops_q,
        "featured_collection": featured_q,
        "new_collections": last_eight_q,
        "featured_drop": featured_drop_q,
        "most_anticipated": ma_drop_q,
        "future_favourite": ff_drop_q
    }
    return render(request, "home-view.html", context=context)
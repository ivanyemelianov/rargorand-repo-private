from django.shortcuts import render

from .models import Drop
def drop_detail_view(request, id=None):
    drop_obj = None
    if id is not None:
        drop_obj = Drop.objects.get(id=id)

    context = {
        "object": drop_obj,
    }
    return render(request, "drops/drop-detail.html", context=context)

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Drop

def drop_search_view(request):
    query_dict = request.GET
    #query = query_dict.get("q")

    try:
        query = int(query_dict.get("q"))
    except:
        query = None

    drop_obj = None
    if query is not None:
        drop_obj = Drop.objects.get(id=query)
    context = {
        "object": drop_obj
    }
    return render(request, "drops/drop-search.html", context=context)

@login_required
def drop_create_view(request):
    context = {}
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        drop_object = Drop.objects.create(title=title, description=description)
        context['objest'] = drop_object
        context['created'] = True   
    return render(request, "drops/drop-create.html", context=context)


def drop_detail_view(request, id=None):
    drop_obj = None
    if id is not None:
        drop_obj = Drop.objects.get(id=id)

    context = {
        "object": drop_obj,
    }
    return render(request, "drops/drop-detail.html", context=context)

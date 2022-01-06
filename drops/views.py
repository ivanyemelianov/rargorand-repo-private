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

def drop_detail_view(request, id=None):
    drop_obj = None
    if id is not None:
        drop_obj = Drop.objects.get(id=id)

    context = {
        "object": drop_obj,
    }
    return render(request, "drops/drop-detail.html", context=context)

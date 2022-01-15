from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect

from .forms import DropForm
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

from django.shortcuts import render
from drops.models import Drop
from ncollections.models import Ncollection


SEARCH_TYPE_MAPPING = {
    'drops': Drop,
    'drop': Drop,
    'nftcollection': Ncollection,
    'nftcollections': Ncollection,

}


def search_view(request):
    query = request.GET.get('q')
    search_type = request.GET.get('type')
    Klass = Ncollection
    if search_type in SEARCH_TYPE_MAPPING.keys():
        Klass = SEARCH_TYPE_MAPPING[search_type]
    qs = Klass.objects.search(query=query)
    context = {
        "queryset": qs
    }
    template = "search/results-view.html"
    if request.htmx:
        context['queryset'] = qs[:5]
        template = "search/partials/results.html"
    return render(request, template, context)
from django.http import HttpResponse
from django.template.loader import render_to_string
from drops.models import Drop

#drop_qs = Drop.objects.all()
#context = {
#    "obj_list": drop_qs,
#}

HTML_STRING = "Hello"#render_to_string("home-view.html", context=context)

def home_view(request, *args, **kwargs):
    return HttpResponse(HTML_STRING)
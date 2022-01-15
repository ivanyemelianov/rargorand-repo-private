import random
from django.http import HttpResponse
from django.template.loader import render_to_string
from drops.models import Drop

<<<<<<< HEAD
drop_qs = Drop.objects.all()
context = {
    "obj_list": drop_qs,
}

HTML_STRING = render_to_string("home-view.html", context=context)
=======
>>>>>>> e3e2775 (Reverse URLs and fixing home view)

def home_view(request, *args, **kwargs):
    """
    Take in a request (Django sends request)
    Return HTML as a response (We pick to return the response)
    """
    name = "Justin" # hard coded
    random_id = random.randint(1, 4) # pseudo random
    
    # from the database??
    drop_obj = Drop.objects.all().first()
    drop_queryset = Drop.objects.all()
    context = {
        "object_list": drop_queryset,
        "object": drop_obj,
    }
    # Django Templates
    HTML_STRING = render_to_string("home-view.html", context=context)
    # HTML_STRING = """
    # <h1>{title} (id: {id})!</h1>
    # <p>{content}!</p>
    # """.format(**context)
    return HttpResponse(HTML_STRING)
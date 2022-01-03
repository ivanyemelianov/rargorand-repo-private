from django.http import HttpResponse

HTML_STRING = "<h1>Hello!</h1>"

def home(request):
    return HttpResponse(HTML_STRING)
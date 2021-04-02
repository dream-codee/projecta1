from django.http import HttpResponse

def demo(request):
    return HttpResponse("<h1>Cest bon ici</h1>")
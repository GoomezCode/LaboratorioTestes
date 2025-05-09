from django.http import HttpResponse

def indexView(request):
    return HttpResponse("<h1>Bem-vindo ao Home</h1>")
    
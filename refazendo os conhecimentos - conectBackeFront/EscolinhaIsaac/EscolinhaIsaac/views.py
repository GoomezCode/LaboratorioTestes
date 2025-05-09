from django.http import HttpResponse

def pageHome(request):
    return HttpResponse("Bem-vindo a escola Issac")
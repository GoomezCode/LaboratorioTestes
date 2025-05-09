from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def tarefasHome(request):
    contexto = {
    "Nome":"Daniel"
    }
    return render(request,"tarefas/home.html", contexto)

def abaLogin(request):
    login = {
        "Nome":"Daniel"
    }
    return render(request, "tarefas/abaLogin.html", login)
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import tarefaModel
from .forms import tarefaForms
# Create your views here.

def tarefasHome(request):
    contexto = {
    "Nome":"Daniel",
    "tarefas":tarefaModel.objects.all()
    }
    return render(request,"tarefas/home.html", contexto)

def abaLogin(request):
    login = {
        "Nome":"Daniel"
    }
    return render(request, "tarefas/abaLogin.html", login)

def adicionarTarefas(request:HttpRequest):
    if request.method == "POST":
        formulario = tarefaForms(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("tarefas:abaHome")

    contexto = {
        "form":tarefaForms
    }
    return render(request, "tarefas/adicionar.html", contexto)
from django.http import HttpResponse
from django.shortcuts import render

def pageHome(request):
    return render(request, "home/index.html")
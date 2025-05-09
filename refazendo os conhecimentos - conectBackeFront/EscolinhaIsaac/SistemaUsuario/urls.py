from django.urls import path
from . import views

app_name = "SistemaUsuario"

urlpatterns = [
    path("cadastro/", views.cadastro)
]

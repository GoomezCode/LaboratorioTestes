from django.urls import path
from . import views

app_name = "tarefas"

urlpatterns = [
    path("", views.tarefasHome, name="abaHome"),
    path("abaLogin/", views.abaLogin, name="abaLogin"),
    path("adicionar/", views.adicionarTarefas)
]
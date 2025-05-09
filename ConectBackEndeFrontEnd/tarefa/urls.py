from django.urls import path
from . import views

app_name = "tarefa"

urlpatterns = [
    path("", views.tarefasHome),
    path("abaLogin/", views.abaLogin, name="abaLogin")
]
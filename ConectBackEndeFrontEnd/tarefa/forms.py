from django import forms
from .models import tarefaModel

class tarefaForms(forms.ModelForm):
    class Meta:
        model = tarefaModel
        fields = ["nome","descricao","completo"]

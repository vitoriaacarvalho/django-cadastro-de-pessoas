from django import forms
from .models import Pessoa, Contato

class PessoaForm(forms.ModelForm):
    nasc=forms.DateField(
        widget=forms.TextInput(
        attrs={"type": "date"}
    )
    )
    class Meta:
        fields= ('__all__')
        model= Pessoa


class ContatoForm(forms.ModelForm):
    class Meta:
        fields = ['nome', 'email', 'telefone']
        model= Contato




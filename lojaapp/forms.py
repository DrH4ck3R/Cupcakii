from django import forms
from django.db.models import fields
from .models import Pedido_order, Cliente
from django.forms import ModelForm, TextInput,EmailInput
from django.contrib.auth.models import User



class Checar_PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido_order
        fields = ["ordenando_por", "endereco_envio", "telefone", "email","pagamento_method"]
        widgets = {
            'ordenando_por': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco_envio': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }







class ClienteRegistrarForm(forms.ModelForm):
    usuario = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=EmailInput(attrs={'class': 'form-control'}))
    nome_completo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    endereco = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Cliente
        fields = ["usuario", "senha", "email", "nome_completo", "endereco"]
        widgets = {
            'usuario': forms.TextInput(attrs={'class': 'form-control'}),
            'senha': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'nome_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
        }


    def clean_usuario(self):
        username = self.cleaned_data.get("usuario")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("ESTE CLIENTE JÁ EXISTE")
        return username




class ClienteEntrarForm(forms.Form):
    usuario = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


#





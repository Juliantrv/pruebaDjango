from django.forms import ModelForm
from django import forms
from .models import Usuario, Oferta, Empresa


class UsuarioForm(ModelForm):
    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date'
            }
        )
    )

    class Meta:
        model = Usuario
        fields = [
            'fecha_nacimiento',
            'profesion',
            'descripcion_perfil',
            'numero_identificacion',
            'celular'
        ]


class OfertaForm(ModelForm):
    class Meta:
        model = Oferta
        fields = [
            'titulo',
            'descripcion',
            'salario',
            'habiliadades'
        ]

class EmpresaForm(ModelForm):
    class Meta:
        model = Empresa
        fields = [
            'nombre',
            'nit',
            'descripcion'
        ]

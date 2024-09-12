from django import forms
from .models import Pais, Cliente
from django.core.exceptions import ValidationError

class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        # fields = ['nombre', 'descripcion']
        fields = '__all__'

    def clean_pais(self):
        pais = self.cleaned_data.get("pais", "")
        #validar que solo tenga letras
        if not pais.isalpha():
            raise ValidationError("El pais solo puede contener letras")
        
        if len(pais) < 3 or len(pais) > 12:
            raise ValidationError("El pais debe tener una longitud minima de e letras o maxima de 12 letras ")
        
        return pais

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        # fields = ['nombre', 'descripcion']
        fields = '__all__'
        widgets = {"nacimiento": forms.DateTimeInput(attrs={"type": "date"})}

    def clean_cliente(self):
        cliente = self.cleaned_data.get("cliente", "")
        #validar que solo tenga letras
        if not cliente.isalpha():
            raise ValidationError("El Cliente solo puede contener letras")
        
        if len(cliente) < 3 or len(cliente) > 12:
            raise ValidationError("El Cliente debe tener una longitud minima de e letras o maxima de 12 letras ")
        
        return cliente
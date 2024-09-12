from django import forms
from .models import ProductosCategoria
from django.core.exceptions import ValidationError

class ProductosCategoriaForm(forms.ModelForm):
    class Meta:
        model = ProductosCategoria
        # fields = ['nombre', 'descripcion']
        fields = '__all__'
    
    def clean_productoscategoria(self):
        productoscategoria = self.cleaned_data.get("Productos Categoria", "")
        #validar que solo tenga letras
        if not productoscategoria.isalpha():
            raise ValidationError("El nombre solo puede contener letras")
        
        if len(productoscategoria) < 3 or len(productoscategoria) > 12:
            raise ValidationError("El nombre debe tener una longitud minima de e letras o maxima de 12 letras ")
        
        return productoscategoria

from django.contrib import admin
from .models import ProductosCategoria, Producto 


admin.site.register(ProductosCategoria)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'nombre','stock', 'unidad_de_medida', 'precio')
    list_filter = ('categoria', 'unidad_de_medida')
    list_display = ('categoria', 'nombre')



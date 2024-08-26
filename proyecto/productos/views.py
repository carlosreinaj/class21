from django.shortcuts import render

from .models import ProductosCategoria

def index(request):
    return render(request, 'productos/index.html')

def ProductosCategoria_list(request):
    productoscategoria = ProductosCategoria.objects.all()
    contexto = {'productoscategoria':productoscategoria }
    return render(request, 'productos/productoscategoria_list.html', contexto)


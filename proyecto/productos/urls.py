from django.urls import path
from .import views

app_name = "productos"

urlpatterns = [
    path("", views.index, name="index"),
    path("productoscategoria/list", views.ProductosCategoria_list, name="productoscategoria_list"),
]
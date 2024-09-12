from django.urls import path
from .import views

app_name = "productos"

urlpatterns = [
    path("", views.index, name="index"),
    #path("productoscategoria/list", views.ProductosCategoria_list, name="productoscategoria_list"),
    path("productoscategoria/list", views.ProductosCategoriaList.as_view(), name="productoscategoria_list"),
    #path("productoscategoria/form", views.ProductosCategoria_form, name="productoscategoria_form"),
    path("productoscategoria/form", views.ProductosCategoriaCreate.as_view(), name="productoscategoria_form"),
    #path("productoscategoria/detail/<int:pk>", views.productoscategoria_detail, name="productoscategoria_detail"),
    path("productoscategoria/detail/<int:pk>", views.ProductosCategoriaDetail.as_view(), name="productoscategoria_detail"),
    #path("productoscategoria/update/<int:pk>", views.productoscategoria_update, name="productoscategoria_update"),
    path("productoscategoria/update/<int:pk>", views.ProductosCategoriaUpdate.as_view(), name="productoscategoria_update"),
    #path("productoscategoria/delete/<int:pk>", views.productocategoria_delete, name="productoscategoria_delete"),
    path("productoscategoria/delete/<int:pk>", views.ProductosCategoriaDelete.as_view(), name="productoscategoria_delete"),
]
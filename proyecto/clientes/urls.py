from django.urls import path
from django.contrib.auth.decorators import login_required

from .import views

app_name = "clientes"

urlpatterns = [
    path("", views.index, name="index"),
    #path("pais/list", views.pais_list, name="pais_list"),
    path("pais/list", login_required(views.PaisList.as_view()), name="pais_list"),
    #path("pais/form", login_required(views.pais_form, name="pais_form"),
    path("pais/form", login_required(views.PaisCreate.as_view()), name="pais_form"),
    #path("pais/detail/<int:pk>", login_required(views.pais_detail, name="pais_detail"),
    path("pais/detail/<int:pk>", login_required(views.PaisDetail.as_view()), name="pais_detail"),
    path("cliente/list", login_required(views.cliente_list), name="cliente_list"),
    path("cliente/form", login_required(views.cliente_form), name="cliente_form"),
]

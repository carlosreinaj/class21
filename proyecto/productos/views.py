from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect
from .forms import ProductosCategoriaForm
from .models import ProductosCategoria
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def index(request):
    return render(request, 'productos/index.html')

#---------------------------- LIST-----------------------
def ProductosCategoria_list(request):
    q = request.GET.get('q')
    if q:
        query = ProductosCategoria.objects.filter(nombre__icontains=q)
    else:
        query = ProductosCategoria.objects.all()
    context = {'object_list': query}
    return render(request, 'productos/productoscategoria_list.html', context)

class ProductosCategoriaList(LoginRequiredMixin, ListView):
    model = ProductosCategoria
    #template_name = 'productos/productoscategoria_list.html'
    #context_object_name = 'categorias'
    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = ProductosCategoria.objects.filter(nombre__icontains=q)
        return queryset

#----------------------------- CREATE----------------------------
def ProductosCategoria_form(request):
    if request.method == 'GET':
        form = ProductosCategoriaForm()

    if request.method == 'POST':
        form = ProductosCategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos:productoscategoria_list')
        
    return render(request, 'productos/productoscategoria_form.html', {'form': form})

class ProductosCategoriaCreate(LoginRequiredMixin, CreateView):
    model = ProductosCategoria
    form_class = ProductosCategoriaForm
    success_url = reverse_lazy('productos:productoscategoria_list')

#------------------ -------DETAIL-----------
def productoscategoria_detail(request, pk: int):
    query = ProductosCategoria.objects.get(id=pk)
    context = {'object': query}
    return render(request, 'productos/productoscategoria_detail.html', context)

class ProductosCategoriaDetail(DetailView):
    model = ProductosCategoria
    #template_name = 'productos/productoscategoria_detail.html'
    #context_object_name = 'object'


#------------------------- UPDATE ------------------------
def productoscategoria_update(request, pk: int):
    query = ProductosCategoria.objects.get(id=pk)
    if request.method == 'GET':
        form = ProductosCategoriaForm(instance=query)

    if request.method == 'POST':
        form = ProductosCategoriaForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect('productos:productoscategoria_list')
        
    return render(request, 'productos/productoscategoria_form.html', {'form': form})

class ProductosCategoriaUpdate(UpdateView):
    model = ProductosCategoria
    form_class = ProductosCategoriaForm
    successful_url = reverse_lazy('productos:productoscategoria_list')

#---------------------- DELETE ------------------------
def productocategoria_delete(request, pk:int):
    query = ProductosCategoria.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        return redirect('productos:productoscategoria_list')
    return render(request, 'productos/productoscategoria_confirm_delete.html', {'object': query})

class ProductosCategoriaDelete(DeleteView):
    model = ProductosCategoria
    success_url = reverse_lazy('productos:productoscategoria_list')


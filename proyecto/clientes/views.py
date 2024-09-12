from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from .forms import PaisForm, ClienteForm
from .models import Pais, Cliente

@login_required
def index(request):
    return render(request, 'clientes/index.html')

#-----------------------------PAIS------------------------------
#----------LIST
def pais_list(request):
    query = request.GET.get('q')
    if query:
        paises = Pais.objects.filter(nombre__icontains=query)
    else:
        paises = Pais.objects.all()
    contexto = {'paises': paises}
    return render(request, 'clientes/pais_list.html', contexto)

class PaisList(ListView):
    model = Pais
    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = Pais.objects.filter(nombre__icontains=q)
        return queryset


#----------CREATE
def pais_form(request):
    if request.method == 'GET':
        form = PaisForm()

    if request.method == 'POST':
        form = PaisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes:pais_list')
    return render(request, 'clientes/pais_form.html', {'form': form})

class PaisCreate(CreateView):
    model = Pais
    form_class = PaisForm
    success_url = reverse_lazy('clientes:pais_list')


#----------DETAIL           
def pais_detail(request, pk:int):    
    query = Pais.objects.get(id=pk)
    context = {'object': query}
    return render(request, 'clientes/pais_detail.html', context)

class PaisDetail(DetailView):
    model = Pais


#---------------------------------CLIENTE--------------------------  
#----------LIST 
def cliente_list(request):
    q = request.GET.get('q')
    if q:
        query = Cliente.objects.filter(nombre__icontains=q)
    else:
        query = Cliente.objects.all()
    context = {'object_list': query}
    return render(request, 'clientes/cliente_list.html', context)

#----------CREATE
def cliente_form(request):
    if request.method == 'GET':
        form = ClienteForm()

    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes:cliente_list')
    return render(request, 'clientes/cliente_form.html', {'form': form})



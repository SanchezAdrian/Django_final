from django.shortcuts import render
from nucleo.models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def ListClientes(request):
    listaClientes = Cliente.objects.all()

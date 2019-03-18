from django.shortcuts import render
from django.utils import timezone
from .models import Recepta

# Mostra un llistat amb totes les receptes.
def llista_receptes(request):
    receptes = Recepta.objects.filter(actiu=True).order_by('data_creacio')
    return render(request, 'receptes/llista_receptes.html', {'receptes':receptes})
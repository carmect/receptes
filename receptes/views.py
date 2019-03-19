from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Recepta

# Mostra un llistat amb totes les receptes.
@login_required
def llista_receptes(request):
    receptes = Recepta.objects.filter(actiu=True).order_by('data_creacio')
    return render(request, 'receptes/llista_receptes.html', {'receptes':receptes})

@login_required    
def recepta_detall(request, pk):
    recepta = get_object_or_404(Recepta, pk=pk)
    return render(request, 'receptes/recepta_detall.html', {'recepta': recepta})
from django.shortcuts import render

# Mostra un llistat amb totes les receptes.
def llista_receptes(request):
    return render(request, 'receptes/llista_receptes.html', {})
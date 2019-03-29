from django import forms

from .models import Recepta

class ReceptaForm(forms.ModelForm):

    class Meta:
        model = Recepta
        fields = ('titol', 'descripcio')
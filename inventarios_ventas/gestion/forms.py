from django import forms
from .models import Venta

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['cantidad']
        widgets = {
            'cantidad': forms.NumberInput(attrs={'min': 1})
        }

from django import forms
from .models import *


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ('quantity',)
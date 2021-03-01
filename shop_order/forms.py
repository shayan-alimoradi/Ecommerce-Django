from django import forms
from .models import *


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('address',)


class CouponForm(forms.Form):
    code = forms.CharField()
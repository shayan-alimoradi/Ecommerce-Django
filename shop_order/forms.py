from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["address"].required = True

    class Meta:
        model = Order
        fields = ("address",)


class CouponForm(forms.Form):
    code = forms.CharField()

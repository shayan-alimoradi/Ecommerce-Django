from django import forms
from .models import Compare, Cart


class CartForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["quantity"].required = True
        self.fields["quantity"].error_messages.update(
            {"required": "This field is required"}
        )

    class Meta:
        model = Cart
        fields = ("quantity",)


class CompareForm(forms.ModelForm):
    class Meta:
        model = Compare
        fields = ("product",)

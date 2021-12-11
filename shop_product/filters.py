import django_filters
from django import forms
from .models import (
    Brand,
    Color,
    Size,
)


class ProductFilter(django_filters.FilterSet):
    CHOICE1 = {("most expensive", "most expensive"), ("most cheap", "most cheap")}
    CHOICE2 = {("newest", "new"), ("oldest", "old")}
    CHOICE3 = {("most sell", "sell"), ("lowest sell", "sell")}

    price_gte = django_filters.NumberFilter(field_name="unit_price", lookup_expr="gte")
    price_lte = django_filters.NumberFilter(field_name="unit_price", lookup_expr="lte")
    brand = django_filters.ModelMultipleChoiceFilter(
        queryset=Brand.objects.values_list('title'), widget=forms.CheckboxSelectMultiple
    )
    color = django_filters.ModelMultipleChoiceFilter(
        queryset=Color.objects.all(), widget=forms.CheckboxSelectMultiple
    )
    size = django_filters.ModelMultipleChoiceFilter(
        queryset=Size.objects.all(), widget=forms.CheckboxSelectMultiple
    )
    unit_price = django_filters.ChoiceFilter(choices=CHOICE1, method="price_filter")
    create = django_filters.ChoiceFilter(choices=CHOICE2, method="create_filter")
    sell = django_filters.ChoiceFilter(choices=CHOICE3, method="sell_filter")

    def price_filter(self, queryset, name, value):
        data = "unit_price" if value == "most cheap" else "-unit_price"
        return queryset.order_by(data)

    def create_filter(self, queryset, name, value):
        data = "created" if value == "oldest" else "-created"
        return queryset.order_by(data)

    def sell_filter(self, queryset, name, value):
        data = "sell" if value == "lowest sell" else "-sell"
        return queryset.order_by(data)

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from shop_order.forms import OrderForm
from shop_product.models import *
from .models import *
from .forms import *


@login_required(login_url='account:sign-in')
def cart_detail(request):
    cart = Cart.objects.filter(user_id=request.user.id)
    form = OrderForm()
    return render(request, 'cart/detail.html', {'cart': cart, 'form': form})


@login_required(login_url='account:sign-in')
def add_cart(request, id):
    url = request.META.get('HTTP_REFERER')
    product = Product.objects.get(id=id)
    if product.status != None:
        var_id = request.POST.get('select')
        data = Cart.objects.filter(user_id=request.user.id, variant_id=var_id)
        if data:
            check = 'yes'
        else:
            check = 'no'
    else:
        data = Cart.objects.filter(user_id=request.user.id, product_id=id)
        if data:
            check = 'yes'
        else:
            check = 'no'
    
    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data['quantity']
            var_id = request.POST.get('select')
            if check == 'yes':
                if product.status is not None:
                    shop = Cart.objects.get(user_id=request.user.id, product_id=id, variant_id=var_id)
                else:
                    shop = Cart.objects.get(user_id=request.user.id, product_id=id)
                shop.quantity += info
                shop.save()
            else:
                Cart.objects.create(user_id=request.user.id, product_id=id, variant_id=var_id,
                quantity=info)
        return redirect(url)


def remove_cart(request, id):
    url = request.META.get('HTTP_REFERER')
    cart = Cart.objects.get(id=id)
    cart.delete()
    return redirect(url)


def add_to_compare_list(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.user.is_authenticated:
        item = get_object_or_404(Product, id=id)
        qs = Compare.objects.filter(user_id=request.user.id, product_id=id)
        if qs.exists():
            messages.error(request, 'This item has already exists in your compare list', 'warning')
        else:
            Compare.objects.create(user_id=request.user.id, product_id=id)
    else:
        item = get_object_or_404(Product, id=id)
        qs = Compare.objects.filter(user_id=None, product_id=id, session_key=request.session.session_key)
        if qs.exists():
            messages.error(request, 'This item has already exists in your compare list', 'warning')
        else:
            if not request.session.session_key:
                request.session.create()
            Compare.objects.create(user_id=None, product_id=id, session_key=request.session.session_key)
    return redirect(url)


def compare_list(request):
    if request.user.is_authenticated:
        data = Compare.objects.filter(user_id=request.user.id)
        return render(request, 'cart/compare_list.html', {'data': data})
    else:
        data = Compare.objects.filter(session_key=request.session.session_key, user_id=None)
        return render(request, 'cart/compare_list.html', {'data': data})

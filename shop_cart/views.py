from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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
    if product.status is not None:
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
        var_id = request.POST.get('select')
        if form.is_valid():
            info = form.cleaned_data['quantity']
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
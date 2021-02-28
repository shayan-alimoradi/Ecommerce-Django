from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from shop_cart.models import *
from .models import *
from .forms import *


@login_required(login_url='account:sign-in')
def order_detail(request, id):
    return render(request, 'order/detail.html')


@login_required(login_url='account:sign-in')
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            order = Order.objects.create(address=data['address'], user_id=request.user.id)
            messages.success(request, 'Order Created Successfully', 'primary')
        cart = Cart.objects.filter(user_id=request.user.id)
        for c in cart:
            OrderItem.objects.create(user_id=request.user.id, order_id=order.id, product_id=c.product_id,
            variant_id=c.variant_id, quantity=c.quantity)
        return redirect('order:detail', order.id)
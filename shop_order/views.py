# Standard library import
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.http import HttpResponse
from django.contrib import messages

# Third-party import
from suds import Client

# Local import
from shop_product.models import (
    Product,
    Variant
)
from shop_cart.models import Cart
from .models import Order, OrderItem, Coupon
from .forms import OrderForm, CouponForm


@login_required(login_url='account:sign_in')
def order_detail(request, id):
    order = Order.objects.get(id=id)
    form = CouponForm()
    return render(request, 'order/detail.html', {'form': form, 'order': order})


@require_POST
@login_required(login_url='account:sign_in')
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


@login_required(login_url='account:sign_in')
def coupon_order(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = CouponForm(request.POST)
        if form.is_valid():
            time = timezone.now()
            data = form.cleaned_data
            try:
                coupon = Coupon.objects.get(code=data['code'], start__lte=time, end__gte=time, active=True)
            except Coupon.DoesNotExist:
                messages.error(request, 'code is invalid or it is expired', 'danger')
                return redirect(url)
            order = Order.objects.get(id=id)
            order.discount = coupon.discount
            order.save()
        return redirect(url)


MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
mobile = '09123456789'  # Optional
CallbackURL = 'http://localhost:8000/order/verify/' # Important: need to edit for realy server.


@login_required(login_url='account:sign_in')
def send_request(request, price, order_id):
    global amount, o_id
    amount = price
    o_id = order_id
    result = client.service.PaymentRequest(MERCHANT, amount, description, request.user.email, mobile, CallbackURL)
    if result.Status == 100:
        return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
    else:
        order = Order.objects.get(id=o_id)
        order.paid = True
        order.save()
        items = OrderItem.objects.filter(order_id=o_id)
        for item in items:
            if item.product.status is not None:
                product = Product.objects.get(id=item.product.id)
                variant = Variant.objects.get(id=item.variant.id)
                variant.amount -= item.quantity
                product.amount -= item.quantity
                product.sell += item.quantity
                variant.save()
                product.save()
            else:
                product = Product.objects.get(id=item.product.id)
                product.amount -= item.quantity
                product.sell += item.quantity
                product.save()
            Cart.objects.filter(user_id=request.user.id).delete()
        return HttpResponse('Error code: ' + str(result.Status))


@login_required(login_url='account:sign_in')
def verify(request):
    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
        if result.Status == 100:
            return HttpResponse('Transaction success.')
        elif result.Status == 101:
            return HttpResponse('Transaction submitted')
        else:
            return HttpResponse('Transaction failed.')
    else:
        return HttpResponse('Transaction failed or canceled by user')
from django.shortcuts import render
from django.db.models import Sum
from django.views import View
from shop_slider.models import *
from shop_cart.models import *


class Index(View):
    template_name = 'base/index.html'

    def get(self, request):
        slider = Slider.objects.all()
        cart_nums = Cart.objects.filter(user_id=request.user.id).aggregate(sum=Sum('quantity'))['sum']
        return render(request, self.template_name, {'slider': slider, 'cart_nums': cart_nums})

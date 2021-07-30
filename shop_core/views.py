# Standard library import
from django.shortcuts import redirect, render
from django.db.models import Sum
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

# Local import
from shop_slider.models import Slider
from shop_cart.models import Cart
from shop_product.models import Product
from . import tasks


class Index(View):
    template_name = 'base/index.html'

    def get(self, request):
        # tasks.send_mail.delay()
        slider = Slider.objects.all()
        cart_nums = Cart.objects.filter(
            user_id=request.user.id).aggregate(sum=Sum('quantity'))['sum']
        latest = Product.objects.order_by('-created')[:6]
        context = {
            'slider': slider, 
            'cart_nums': cart_nums, 
            'latest': latest
        }
        return render(request, self.template_name, context)


class BucketList(LoginRequiredMixin, View):
    template_name = 'base/bucket.html'
    login_url = 'account:sign-in'

    def get(self, request):
        objects = tasks.get_objects_list_tasks()
        return render(request, self.template_name, {'objects': objects})

    
class DeleteBucket(LoginRequiredMixin, View):
    login_url = 'account:sign-in'

    def get(self, request, key):
        tasks.delete_object_tasks.delay(key)
        messages.success(request, 'Your demand wil be answered soon', 'success')
        return redirect(request.META.get('HTTP_REFERER'))


class DownloadBucket(LoginRequiredMixin, View):
    login_url = 'account:sign-in'

    def get(self, request, key):
        tasks.download_object_tasks.delay(key)
        messages.success(request, 'Your demand wil be answered soon', 'success')
        return redirect(request.META.get('HTTP_REFERER'))


class ProgressBar(View):
    template_name = 'base/progress.html'

    def get(self, request):
        task = tasks.go_to_sleep.delay(1)
        return render(request, self.template_name, {'task_id': task.task_id})
from django.shortcuts import render
from django.views import View
from shop_slider.models import *


class Index(View):
    template_name = 'base/index.html'

    def get(self, request):
        slider = Slider.objects.all()
        return render(request, self.template_name, {'slider': slider})

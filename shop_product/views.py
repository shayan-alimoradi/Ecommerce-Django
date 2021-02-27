from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views import View
from django.db.models import Q
from .models import *
from .forms import *


class ProductList(View):
    template_name = 'product/product_list.html'
    
    def get(self, request, slug=None):
        products = Product.objects.filter(available=True)
        paginator = Paginator(products, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        categories = Category.objects.filter(is_sub=False)
        if slug:
            category = get_object_or_404(Category, slug=slug)
            page_obj = products.filter(category=category)
        form = SearchForm()
        if 'search' in request.GET:
            form = SearchForm(request.GET)
            if form.is_valid():
                data = form.cleaned_data['search']
                page_obj = products.filter(
                    Q(title__icontains=data) |
                    Q(description__icontains=data)
                )
        context = {
            'form': form,
            'products': page_obj,
            'categories': categories
        }
        return render(request, self.template_name, context)


def product_detail(request, slug, id):
    product = get_object_or_404(Product, slug=slug, id=id)
    if product.status is not None:
        if request.method == 'POST':
            variant = Variant.objects.filter(product_variant_id=id)
            var_id = request.POST.get('select')
            variants = Variant.objects.get(id=var_id) 
        else:
            variant = Variant.objects.filter(product_variant_id=id)
            try:
                variants = Variant.objects.get(id=id)
            except Variant.DoesNotExist:
                variants = None
        context = {'product': product, 'variant': variant, 'variants': variants}
        return render(request, 'product/product_detail.html', context)
    else:
        return render(request, 'product/product_detail.html', {'product': product})
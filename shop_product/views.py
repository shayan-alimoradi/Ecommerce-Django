from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Max, Min
from django.views import View
from django.db.models import Q
from django.contrib import messages
from urllib.parse import urlencode
from shop_cart.forms import *
from .models import *
from .forms import *
from .filters import *


class ProductList(View):
    template_name = 'product/product_list.html'
    
    def get(self, request, slug=None):
        products = Product.objects.filter(available=True)
        f = ProductFilter(request.GET, queryset=products)
        products = f.qs
        mx = Product.objects.aggregate(unit_price=Max('unit_price'))
        max_price = str(mx['unit_price'])
        mn = Product.objects.aggregate(unit_price=Min('unit_price'))
        min_price = str(mn['unit_price'])
        compare_form = CompareForm()
        paginator = Paginator(products, 3)
        page_number = request.GET.get('page')
        data = request.GET.copy()
        if 'page' in data:
            del data['page']
        page_obj = paginator.get_page(page_number)
        categories = Category.objects.filter(is_sub=False)
        if slug:
            category = get_object_or_404(Category, slug=slug)
            page_obj = products.filter(category=category)
            paginator = Paginator(page_obj, 3)
            page_number = request.GET.get('page')
            data = request.GET.copy()
            if 'page' in data:
                del data['page']
            page_obj = paginator.get_page(page_number)
        form = SearchForm()
        if 'search' in request.GET:
            form = SearchForm(request.GET)
            if form.is_valid():
                info = form.cleaned_data['search']
                page_obj = products.filter(
                    Q(title__icontains=info) |
                    Q(description__icontains=info) |
                    Q(tag__title__icontains=info)
                )
                paginator = Paginator(page_obj, 3)
                page_number = request.GET.get('page')
                data = request.GET.copy()
                if 'page' in data:
                    del data['page']
                page_obj = paginator.get_page(page_number)
        context = {
            'form': form,
            'products': page_obj,
            'categories': categories,
            'compare_form': compare_form,
            'filter': f,
            'max_price': max_price,
            'min_price': min_price,
            'data': urlencode(data)
        }
        return render(request, self.template_name, context)


def product_detail(request, slug, id):
    product = get_object_or_404(Product, slug=slug, id=id)
    is_fav = False
    if product.favourite.filter(id=request.user.id).exists():
        is_fav = True
    form = CartForm()
    comment_form = CommentForm()
    comment = Comment.objects.filter(product_id=id, is_reply=False, status=True)
    ip_address = request.user.ip_address
    if ip_address not in product.visit_count.all():
        product.visit_count.add(ip_address)
    if product.status is not None:
        if request.method == 'POST':
            variant = Variant.objects.filter(product_variant_id=id)
            var_id = request.POST.get('select')
            variants = Variant.objects.get(id=var_id) 
            colors = Variant.objects.filter(product_variant_id=id, size_variant_id=variants.size_variant_id)
            size = Variant.objects.filter(product_variant_id=id).distinct('size_variant_id')
        else:
            variant = Variant.objects.filter(product_variant_id=id)
            variants = Variant.objects.get(id=id)
            colors = Variant.objects.filter(product_variant_id=id, size_variant_id=variants.size_variant_id)
            size = Variant.objects.filter(product_variant_id=id).distinct('size_variant_id')
        context = {'product': product, 'variant': variant, 'variants': variants,
        'form': form, 'comment_form': comment_form, 'comment': comment,
        'is_fav': is_fav, 'colors': colors, 'size': size}
        return render(request, 'product/product_detail.html', context)
    else:
        context = {
            'product': product, 'form': form, 'comment_form': comment_form,
            'comment': comment, 'is_fav': is_fav
        }
        return render(request, 'product/product_detail.html', context)


@login_required(login_url='account:sign-in')
def add_comment(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Comment.objects.create(user_id=request.user.id, comment=data['comment'],
            product_id=id)
            messages.success(request, 'after we accept, your comment will show on site', 'primary')
        return redirect(url)


@login_required(login_url='account:sign-in')
def add_favourite(request, id):
    url = request.META.get('HTTP_REFERER')
    product = get_object_or_404(Product, id=id)
    is_fav = False
    if product.favourite.filter(id=request.user.id).exists():
        product.favourite.remove(request.user)
        is_fav = False
    else:
        product.favourite.add(request.user)
        is_fav = True
    return redirect(url)


@login_required(login_url='account:sign-in')
def favourite_list(request):
    fa_product = request.user.fav.all()
    paginator = Paginator(fa_product, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'product/fav_list.html', {'product': page_obj})


def page_not_found(request, exception=None):
    return render(request, 'product/404.html')
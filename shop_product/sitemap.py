from django.contrib.sitemaps import Sitemap
from .models import Product

class ProductSitemap(Sitemap):
    changefreq = "daily"
    priority = 1

    def items(self):
        return Product.objects.filter(available=True)

    def lastmod(self, obj):
        return obj.updated
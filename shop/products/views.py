from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views.generic import ListView
from products.models import Product


class IndexView(TemplateView):
    template_name = "index.html"


class ProductListView(ListView):
    model = Product
    paginate_by = 10


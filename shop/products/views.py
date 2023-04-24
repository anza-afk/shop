from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views.generic import ListView
from products.models import Product
from cart.forms import CartAddProductForm

class IndexView(TemplateView):
    template_name = "index.html"


class ProductListView(ListView):
    model = Product
    paginate_by = 5
    
    def get_context_data(self,**kwargs):
        context = super(
            ProductListView,self).get_context_data(**kwargs)
        context['cart_product_form']=CartAddProductForm(self.request.GET or None)
        return context
from django.urls import path

from products.views import (
    IndexView,
    ProductListView
)

urlpatterns = [
    path(
        '',
        IndexView.as_view(),
        name='index'
    ),
    path(
        'catalog/',
        ProductListView.as_view(),
        name='product_list'
    ),
]

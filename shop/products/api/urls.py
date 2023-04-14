from django.urls import path

from products.api.views import (
    ProductListView,
    CategoryListView
)

urlpatterns = [
    path(
        'all/',
        ProductListView.as_view(),
        name='product_list'
    ),
    path(
        'categories/',
        CategoryListView.as_view(),
        name='category_list'
    ),
]

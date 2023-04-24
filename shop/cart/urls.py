from django.urls import path
from . import views


urlpatterns = [
    path(r'^$', views.CartDetail, name='CartDetail'),
    path(r'^remove/(?P<product_id>\d+)/$', views.CartRemove, name='CartRemove'),
    path(r'^add/(?P<product_id>\d+)/$', views.CartAdd, name='CartAdd'),
]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='home'),
    path('product/<slug:slug>', views.product_Details, name='product_detail'),

    # error page
    path('404', views.error404, name='404'),
]
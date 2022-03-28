from itertools import product
from django.shortcuts import redirect, render
from .models import Slider, Banner_Area, Main_Category, Category, Sub_Category, Product

def homepage(request):
    slider = Slider.objects.all().order_by('-id')[0:3]
    banner = Banner_Area.objects.all().order_by('-id')[0:3]
    main_category = Main_Category.objects.all()
    products = Product.objects.filter(section__name = 'Top Deals Of The Day')

    context = {
        'sliders': slider,
        'banners': banner,
        'main_category': main_category,
        'products': products,
    }
    return render(request, 'main/home.html', context)

def product_Details(request, slug):
    product = Product.objects.filter(slug=slug)

    if product.exists():
        product = Product.objects.get(slug=slug)
    else:
        return redirect('404')

    context = {
        'product': product,
    }
    return render(request, 'product/product_detail.html', context)


def error404(request):
    return render(request, 'errors/404.html')
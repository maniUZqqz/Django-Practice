from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Product, ProductCategory
from django.db.models import Avg, Max, Min, Count, Sum


def product_list(request):
    # consol = ProductCategory(
    #     title='Consol', url="p-m"
    # )
    # consol.save()
    # mobile_S = Product(title="S21", price=4245, rating=4, category=consol)
    # mobile_S.save()
    products = Product.objects.all().order_by('title')
    number_of_products = products.count()
    avg_rating = products.aggregate(
        Avg('rating'),
        Max('rating'),
        Min('rating'),
        Max('price'),
        Min('price'),
    )
    return render(
        request,
        'myapp/product_list.html',
        {
            'products': products,
            'total_number_of_products': number_of_products,
            'average_ratings': avg_rating
        }
    )



def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(
        request,
        'myapp/product_detail.html',
        {'product': product}
    )

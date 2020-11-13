from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def all_products(request):
    '''a view to show all products, include sort & search'''

    products = Product.objects.all()

    context = {
        'products': products,
    }
    
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    '''a view to show individual product'''

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    
    return render(request, 'products/product_detail.html', context)

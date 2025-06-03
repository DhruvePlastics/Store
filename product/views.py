from django.shortcuts import render, get_object_or_404
from .models import Product
from django.core.paginator import Paginator

def home(request):
    featured_products = Product.objects.filter(is_featured=True, is_active=True).order_by('-id')[:6]
    
    # Example static testimonials, replace with your actual source if any
    testimonials = [
        {'text': 'Great product!', 'author': 'Alice', 'rating': 5},
        {'text': 'Fast delivery and excellent quality.', 'author': 'Bob', 'rating': 4},
        {'text': 'Amazing customer support!', 'author': 'Charlie', 'rating': 5},
    ]
    
    context = {
        'featured_products': featured_products,
        'testimonials': testimonials,
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def product_list(request):
    products = Product.objects.filter(is_active=True).order_by('name')  # example ordering
    paginator = Paginator(products, 6)  # 6 products per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'product_list.html', {'page_obj': page_obj})

def product_detail(request, sku):
    product = get_object_or_404(Product, sku=sku)
    return render(request, 'product_detail.html', {'product': product})

# En makeup/views.py

from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductForm

def productos(request):
    products = Product.objects.all()
    return render(request, 'mymakeupstore\templates\mymakeupstore\templates', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', )

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProductForm()

    return render(request, 'create_product.html', {'form': form})



# En tu archivo views.py
from django.shortcuts import render



from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import ProductForm
from .models import Product

# Create your views here.

def index(request):
    status = ''
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ProductForm()
        return render(request, 'honda/index.html', {'form': form, 'products': Product.objects.all(), 'status': status })

def edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    status = 'success'
    titleValue = Product.objects.filter(pk=pk).values('title')[0];
    product_title = titleValue['title']
    
    if request.method == 'POST':
        post_form = ProductForm(request.POST, instance=product)
        if post_form.is_valid():
            post_form.save()
            return render(request, 'honda/edit.html', {'form': post_form, 'status': status, 'product_title': product_title })
    else:
        form = ProductForm(instance=product)
        return render(request, 'honda/edit.html', {'form': form, 'product_title': product_title })

def delete(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return HttpResponseRedirect('/')

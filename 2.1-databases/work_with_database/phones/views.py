from django.shortcuts import render, redirect
from .models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_by = request.GET.get('sort')
    if sort_by == 'name':
        context = {'phones': Phone.objects.order_by('name')}
    elif sort_by == 'min_price':
        context = {'phones': Phone.objects.order_by('price')}
    elif sort_by == 'max_price':
        context = {'phones': Phone.objects.order_by('-price')}
    else:
        context = {'phones': Phone.objects.all()}

    template = 'catalog.html'
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.get(slug=slug)}
    return render(request, template, context)

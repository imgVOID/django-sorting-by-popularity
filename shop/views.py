from django.shortcuts import render, get_object_or_404
from shop.models import Product, ProductType
from django.http import HttpResponseRedirect

# Create your views here.
def all_list(request):
    tvs = Product.objects.filter(product_type__title='Телевизор').order_by('-popularity')
    fridges = Product.objects.filter(product_type__title='Холодильник').order_by('-popularity')
    return render(request, 'all_list.html', {'tvs':tvs, 'fridges':fridges})

def adding_some_popularity(request, pk):
    item = get_object_or_404(Product, id=pk)
    item.popularity += 1
    item.save()
    return HttpResponseRedirect('/')
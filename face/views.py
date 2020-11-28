from django.shortcuts import render
from products.models import Product
#from django.http import HttpResponse
# Create your views here.
#def test1(request):
   # return HttpResponse("<h1>sami</h1>")
def index(request):
    context={
        'products':Product.objects.all()
    }
    return render(request,'pages/index.html',context)
def about (request):
    return render(request,'pages/about.html')
def coffee(request):
    return render(request,'pages/coffee.html')
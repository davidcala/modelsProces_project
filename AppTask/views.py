from django.shortcuts import render
from AppTask import models
# Create your views here.
def home(request):
    producto = models.Product.objects.all()
    return render(request, 'home.html', {
        'productos': producto,
    })


def categories(request):
    categories = models.Category.objects.all()

    return render(request, 'categories.html', {
        'categories': categories,
    })

def tags(request):
    tags= models.Tag.objects.all()

    return render(request, 'tags.html', {
        'tags': tags,
    })

def productdetail(request,id):
    producto = models.Product.objects.get(id=id)
    print(producto)

    return render(request, 'producdetail.html', {
        'product': producto,
    })

def categoriesdetail(request,id):
    category = models.Category.objects.get(id=id)
    return render(request, 'categoriesdetail.html', {
        'category': category,
    })
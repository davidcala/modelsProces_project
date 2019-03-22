from django.shortcuts import render
from AppTask import models
# Create your views here.
def home(request):
    return render(request, 'home.html')


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

def product1(request):
    return render(request, 'product1.html')

def product2(request):
    return render(request, 'product2.html')
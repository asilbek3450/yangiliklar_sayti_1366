from django.shortcuts import render
from .models import Category, News

# Create your views here.
def home_page(request):
    kategoriyalar = Category.objects.all()
    yangiliklar = News.objects.all()
    context = {
        'kategoriyalar': kategoriyalar,
        'yangiliklar': yangiliklar
    }
    return render(request, template_name='index.html', context=context)


def single_post(request, pk):
    kategoriyalar = Category.objects.all()
    yangilik = News.objects.get(id=pk)
    context = {
        'kategoriyalar': kategoriyalar,
        'yangilik': yangilik
    }
    return render(request, template_name='singlepost.html', context=context)
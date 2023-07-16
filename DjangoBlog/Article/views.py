from django.shortcuts import render, HttpResponse
from .models import Article


def opening_page(request):
    return render(request, 'opening_page.html')

def articles_list(request):
    articles_list = Article.objects.all().order_by('-published')
    return render(request, 'articles.html', {'articles_list': articles_list})
from django.shortcuts import render, HttpResponse


def opening_page(request):
    return render(request, 'opening_page.html')

def article_list(request):
    articles = "New article"
    return render(request, 'articles.html', {'articles': articles})
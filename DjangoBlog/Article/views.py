from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Article
from .forms import UserRegistrationForm, ArticleAddingForm, UpdateArticle


def opening_page(request):
    return render(request, 'opening_page.html')

def articles_list(request):
    articles_list = Article.objects.all().order_by('-published')
    return render(request, 'articles.html', {'articles_list': articles_list})

def articles_details(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'details.html', {'article': article})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            
            new_user.save()
            
            return render(request, 'account/register_done.html', {'user_form': user_form})
    else:
        user_form = UserRegistrationForm()
        
    return render(request, 'account/register.html', {'user_form': user_form})

def article_form(request):
    article_form = ArticleAddingForm(request.POST)
    
    if request.method == 'POST':
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.author = request.user
            article = article_form.save()
            
            return redirect('article_list')
    else:
        article_form = ArticleAddingForm()
        
    return render(request, 'account/add_article.html', {'article_form': article_form})

def update_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    update_article_form = UpdateArticle(request.POST or None, instance=article)
    
    if update_article_form.is_valid():
        update_article_form.save()
        
        return redirect('article_list')
    else:
        update_article_form = UpdateArticle()
        
    return render(request, 'account/update_article.html', {'update_article_form': update_article_form, 'article': article})

def delete_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    
    if article:
        article.delete()
        return render(request, 'account/delete_article.html', {'article': article})
    
    return render()
        
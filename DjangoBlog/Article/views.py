from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Article
from .forms import UserRegistrationForm


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
        
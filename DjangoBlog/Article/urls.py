from django.urls import path
from .views import opening_page, articles_list, articles_details, register
from django.contrib.auth.views import LoginView


urlpatterns = [
    # path('', opening_page, name='opening_page'),
    path('', LoginView.as_view(), name='login'),
    path('articles/', articles_list, name='article_list'),
    path('articles/<slug:slug>/', articles_details, name='article_details'),
    path('register/', register, name='register'),
]

from django.urls import path
from .views import opening_page, article_list


urlpatterns = [
    path('', opening_page, name='opening_page'),
    path('articles/', article_list, name='article_list'),
]

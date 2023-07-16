from django.urls import path
from .views import opening_page, articles_list


urlpatterns = [
    path('', opening_page, name='opening_page'),
    path('articles/', articles_list, name='article_list'),
]

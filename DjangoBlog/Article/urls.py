from django.urls import path
from .views import (
    opening_page, 
    articles_list, 
    articles_details, 
    register,
    article_form,
    update_article,
    delete_article,
)

from django.contrib.auth.views import (
    LoginView, 
    LogoutView, 
    PasswordChangeView, 
    PasswordChangeDoneView
)


urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('articles/', articles_list, name='article_list'),
    path('articles/<slug:slug>/', articles_details, name='article_details'),
    path('register/', register, name='register'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change-done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('add-article/', article_form, name='article_form'),
    path('update-article/<slug:slug>/', update_article, name='update_article_form'),
    path('deleted-article/<slug:slug>/', delete_article, name='deleted_article'),
]

from django.contrib.auth.models import User
from django import forms
from .models import Article


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not matching')
        return cd['password2']


class ArticleAddingForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'desc')

class UpdateArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'desc')


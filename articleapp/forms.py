from django.forms import ModelForm, forms
from django import forms
from articleapp.models import Article

class ArticleCreationForm(ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']
from django.forms import ModelForm, forms
from questionapp.models import Question
from django import forms


class QuestionCreationForm(ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'image', 'content']


class QuestionSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')
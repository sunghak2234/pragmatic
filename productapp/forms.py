from django.forms import ModelForm
from productapp.models import Product


class ProductCreationForm(ModelForm):

    class Meta:
        model = Product
        fields = ['title', 'file']
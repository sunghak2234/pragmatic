from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, ListView, DeleteView
from productapp.forms import ProductCreationForm
from productapp.models import Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductCreationForm
    context_object_name = 'target_product'
    template_name = 'products/create.html'
    success_url = reverse_lazy('productapp:list')


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'target_product'
    template_name = 'products/detail.html'


class ProductListView(ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'products/list.html'

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/delete.html'

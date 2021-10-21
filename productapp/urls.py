from django.urls import path

from productapp.views import ProductCreateView, ProductListView, ProductDeleteView, ProductDetailView

app_name = 'productapp'

urlpatterns = [
    path('creates/', ProductCreateView.as_view(), name='create'),
    path('list/', ProductListView.as_view(), name='list'),
    path('details/<int:pk>', ProductDetailView.as_view(), name='detail'),

    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete'),

]
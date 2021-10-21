from django.urls import path
from django.views.generic import TemplateView

app_name = 'introapp'

urlpatterns = [
    path('us/', TemplateView.as_view(template_name='intro.html'), name='intro'),
    path('teaminfo/', TemplateView.as_view(template_name='teaminfo.html'), name='teaminfo'),
    path('product/', TemplateView.as_view(template_name='product.html'), name='product'),
    path('test/', TemplateView.as_view(template_name='test.html'), name='test'),

]

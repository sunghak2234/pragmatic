from django.urls import path

from questionapp.views import QuestionCreateView, QuestionDetailView, QuestionListView, QuestionDeleteView
from . import views

app_name = 'questionapp'

urlpatterns = [
    path('create/', QuestionCreateView.as_view(), name='create'),
    path('detail/<int:pk>', QuestionDetailView.as_view(), name='detail'),
    path('list/', QuestionListView.as_view(), name='list'),
    path('delete/<int:pk>', QuestionDeleteView.as_view(), name='delete'),
    path('search/', views.SearchFormView.as_view(), name='search'),
]
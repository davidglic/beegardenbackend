from django.urls import path
from . import views

urlpatterns = [
    path('articles/<str:type>/', views.get_articles, name='get_articles'),
    ]
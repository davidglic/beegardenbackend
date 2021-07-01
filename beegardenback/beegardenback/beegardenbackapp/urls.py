from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_articles, name='get_articles'),
    ]
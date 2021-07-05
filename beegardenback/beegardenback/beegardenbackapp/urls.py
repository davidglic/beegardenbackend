from django.urls import path
from . import views

urlpatterns = [
    path('articles/<str:type>/', views.get_articles, name='get_articles'),
    path('articles/get/<int:id>', views.get_an_article),
    path('login/', views.login),
    path('update/', views.update_user),
    path('create/', views.create_user)
    ]
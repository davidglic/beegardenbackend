from django.urls import path
from . import views

urlpatterns = [
    path('articles/<str:type>/', views.get_articles, name='get_articles'),
    path('login/', views.login),
    path('update/', views.update_user),
    path('create/', views.create_user)
    ]
from django.urls import path
from . import views

urlpatterns = [
    
    path('sendver/<int:id>', views.send_verification)
    ]
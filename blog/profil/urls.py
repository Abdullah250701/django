from django.urls import path
from . import views

urlpatterns = [
    path('Rijaldi', views.home, name='home'),
    
      
]
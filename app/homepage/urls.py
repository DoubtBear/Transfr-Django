from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage-home'),
    path('about/', views.about, name='homepage-about'),
    path('contact/', views.contact, name="homepage-contact"),
]
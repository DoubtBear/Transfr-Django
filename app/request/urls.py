from django.urls import path
from . import views
from .views import RequestCreateView, RequestDetailView


urlpatterns = [
    path('', views.welcome, name="request-welcome"),
    path('create/', views.rides, name="request-form"),
    path('viewpending/<int:pk>', RequestDetailView.as_view() , name="request-viewDetail"),
    path('viewpending', views.viewRides , name="request-view"),
    path('deleterequest/<int:pk>', views.deleteRequest, name="delete-request"),
]
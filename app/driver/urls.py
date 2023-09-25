from django.urls import path

from . import views
from .views import RequestDetailView, AssignedRequestDetailView

urlpatterns = [
    path('', views.welcome, name='driver-welcome'),
    path('rides/', views.rides, name='driver-rides'),
    path('rides/<int:pk>/', RequestDetailView.as_view() , name="driver-viewDetail"),
    path('assigned/<int:pk>/', AssignedRequestDetailView.as_view() , name="driver-viewAssignedDetail"),
    path('assigned/', views.assignedRides, name='driver-assigned'),
    path('summary/', views.summary, name="driver-summary"),
    path('rides/confirmation', views.ridesConfirmation, name="driver-ridesConfirmation"),
    path('close/<int:pk>', views.closeRideView, name="driver-close"),
    path('viewpayments/', views.displayPayment, name="driver-payment")
]

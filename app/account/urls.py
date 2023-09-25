from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='account-home'),
    path('update/', views.update, name='account-update'),
    path('requests/', views.requests, name="account-requests"),
    path('deleteaccount/<int:pk>', views.deleteAccount, name="delete-account"),
    path('updateprofilepic/', views.profileupdate, name="profile-update")
]
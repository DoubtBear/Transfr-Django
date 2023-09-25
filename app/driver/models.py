from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

#Create your models here.

#this is the table for the assigned rides. It's the same as the Post table, but it has a driver column as well
class AssignedRides(models.Model):
    riderLocation = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    date = models.DateTimeField()
    date_created = models.DateTimeField(default=timezone.now)
    riderID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rider')
    driver = models.ForeignKey(User, default=None, on_delete=models.SET_DEFAULT, related_name='driver')
    addSupport = models.CharField(max_length=200, null=True)
    tip = models.DecimalField(decimal_places=2, max_digits=5, null=True)


    def __str__(self):
        return self.destination
    
    def get_absolute_url(self):
        
        return reverse('driver-rides', kwargs={'pk': self.pk})

class DriverPayment(models.Model):
    driver = models.OneToOneField(User, on_delete=models.CASCADE)
    dollars = models.DecimalField(default=0.00, decimal_places=2, max_digits=7 )

    def __str__(self):
        return f'{self.driver} ${self.dollars}'
    
    
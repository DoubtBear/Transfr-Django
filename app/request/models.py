from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
#this is where are table is created and managed. These are our fields and the values we have.
class Post(models.Model):
    riderLocation = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    date = models.DateTimeField()
    date_created = models.DateTimeField(default=timezone.now)
    rider = models.ForeignKey(User, on_delete=models.CASCADE, related_name='riderpending')
    addSupport = models.CharField(max_length=200, null=True)
    tip = models.DecimalField(decimal_places=2, max_digits=5, null=True, default=0.00)

    def __str__(self):
        return self.destination
    
    def get_absolute_url(self):
        
        return reverse('request-viewDetail', kwargs={'pk': self.pk})
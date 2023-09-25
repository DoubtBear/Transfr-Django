from request.models import Post
from .models import AssignedRides, DriverPayment
from django.utils import timezone
import decimal


#this is also a Cody file, django didn't create this. I created this to decentralize the database further.


#this function takes in the request, and the postID which is the **kwargs.get("pk") which is the primary key of the request in Post table
#its quering the database where the primary key is exactly the key passed in, the .get() to make it not a queryset.
#after that it's creating an object in the AssignedRides table and saving it.
#I need to add where this deletes the request from the Post table.
def assignDriver(request, postID):
    requestObject = Post.objects.filter(pk__exact=postID).get()

    driverRequest = AssignedRides(
    riderLocation = requestObject.riderLocation,
    destination = requestObject.destination,
    date = requestObject.date,
    tip = requestObject.tip,
    riderID = requestObject.rider,
    driver = request.user,
    addSupport = requestObject.addSupport, 

    )

    driverRequest.save()
    requestObject.delete()


def closeRide(postID):
    ride = AssignedRides.objects.filter(pk__exact=postID).get()

    

    return ride


def paymentCal(request, distance, key):

   

    ride = AssignedRides.objects.filter(pk__exact=key).get()
    paymentObject = DriverPayment.objects.filter(driver__exact=request.user).get()

    
    payout = distance * decimal.Decimal('.50')

    if ride.tip != None:
        payout += ride.tip

    
    paymentObject.dollars += payout 

    paymentObject.save(update_fields=['dollars'])
    
    ride.delete()
    
    

    
    

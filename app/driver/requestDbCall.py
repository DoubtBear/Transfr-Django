from request.models import Post
from .models import AssignedRides, DriverPayment


#this is my own .py file I made and it's not from django.
#It's purpose is to get the database calls as far from the client as possible for security.
#it imports the model from the requests app and the models from the driver app. 
 
#this generates this list of open request the driver can select from
def RequestListRender():
    requestListAll = Post.objects.all()

    requestListDict = {
        "requestList": requestListAll
    }

    return requestListDict


#this creates the list of requests the driver has accepted. The userID the from the views.py
def AssignedRender(userID):
    assignedRequestList = AssignedRides.objects.filter(driver__exact=userID)

    aRD = {
        "requestList": assignedRequestList
    }
    return aRD

def PaymentRender(user):

    paymentObject = DriverPayment.objects.filter(driver__exact=user).get()

    pDO = {
        "paymentObject": paymentObject
    }

    return pDO
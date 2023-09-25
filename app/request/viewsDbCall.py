from .models import Post
from django.utils import timezone



def RequestRender(userID):
    #this thing works but VS code is dumb and doesn't think it does. NO ERROR!!
    requestList = Post.objects.filter(rider__exact= userID)
    
    return requestList


def WorkAround(form, request):

    

    requestDoc = Post(
    riderLocation = form.cleaned_data.get('riderLocation'),
    destination = form.cleaned_data.get('destination'),
    date = form.cleaned_data.get('date'),
    rider = request.user,
    addSupport = form.cleaned_data.get('addSupport'),
    tip = form.cleaned_data.get('tip')
    )
   
    try:
        requestDoc.save()
        return True
    except:
        return False    


def DeleteRequest(requestID):
    requestToDelete = Post.objects.filter(pk__exact=requestID).get()
    
    try:
        requestToDelete.delete()
        return True
    except:
        return False

    
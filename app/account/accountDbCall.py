from driver.models import AssignedRides
from django.contrib.auth.models import User
from user.models import Profile
from django.contrib import messages

def AssignedRender(userID):
    userRidesObject = AssignedRides.objects.filter(riderID_id__exact=userID)

    userRidesDict = {
        "assignedRides": userRidesObject
    }

    return userRidesDict

def DeleteAccount(userPK):
    userToDelete = User.objects.filter(pk__exact=userPK).get()


    userToDelete.delete()

    return True

def UpdateAccount(form, userID):

    updatedUserObject = User.objects.get(id=userID)

    updatedUserObject.email = form.cleaned_data.get('email')
    updatedUserObject.first_name = form.cleaned_data.get('first_name')
    updatedUserObject.last_name = form.cleaned_data.get('last_name')
    try:
        updatedUserObject.save(update_fields=['email', 'first_name', 'last_name'])
        return True
    except:
        return False

def ProfileUpdate(image, userIn):
    try:
        profile = Profile.objects.filter(user__exact=userIn).get()

    except:
        return False
    
    profile.picture = image

    try:
        profile.save(update_fields=['picture'])

    except:
        return False

    return True
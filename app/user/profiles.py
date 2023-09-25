from .models import Profile
from django.contrib.auth.models import User
from django.contrib import messages


def CreateProfile(userIncoming):
    if Profile.objects.filter(user__exact=userIncoming).exists():
        return False
    userObject = User.objects.filter(pk__exact=userIncoming.id).get()
    print(userObject)
    newProfile = Profile(
        user = userObject,
    )
    try:
        newProfile.save()
        return True
    except:
        
        return False


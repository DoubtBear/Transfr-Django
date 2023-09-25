from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import UserRegisterFormT


from .profiles import CreateProfile
from .decorators import unauthenticated_user



# Create your views here.

@unauthenticated_user
def register(request):
    if request.method == 'POST':
        
        form = UserRegisterFormT(request.POST)
        
        if form.is_valid():

            form.save()
            username = form.cleaned_data.get('username')
            
            
            messages.success(request, f'Congrats! Account Created for {username}! Login with your new account!')
            return redirect('login')
        
            
            
        

    elif request.method == 'GET':
        
        form = UserRegisterFormT()    
    return render(request, 'user/register.html', {'form': form})


def createProfile(request):
    if CreateProfile(request.user):
        return redirect('account-home')
    else:
        messages.error(request,'You already have a profile, don\'t try to make another one')
        return redirect('account-home')
    
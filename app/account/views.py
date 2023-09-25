from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .accountDbCall import AssignedRender, DeleteAccount, UpdateAccount, ProfileUpdate
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from user.models import Profile


# Create your views here.
@login_required
def home(request):
    if Profile.objects.filter(user__exact=request.user).exists():
        return render(request, 'account/summary.html')
    elif not Profile.objects.filter(user__exact=request.user).exists():
        return redirect('create-profile')
    


@login_required
def profileupdate(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            #if ProfileUpdate(form.cleaned_data.get('picture'), request.user):
            messages.success(request, f'Profile Picture Successfully Updated!')
            return redirect('account-home')

    elif request.method == 'GET':
        updateForm = ProfileUpdateForm()

        context = {
            'updateForm': updateForm
        }

        return render(request, 'account/profileupdate.html', context)



@login_required
def deleteAccount(request, **kwargs):
    if DeleteAccount(kwargs.get('pk')):
        messages.error(request, f'Account Succesfully Deleted.. See you later ...?')
        return redirect('homepage-home')


@login_required
def update(request):
    if request.method == 'POST':
        updateForm = UserUpdateForm(request.POST)
        if updateForm.is_valid():
            if UpdateAccount(updateForm, request.user.id):
                messages.success(request, f'Account Details Successfully Updated!')
                return redirect('account-home')
    elif request.method == 'GET':
        updateForm = UserUpdateForm(instance=request.user)

        context = {
            'updateForm': updateForm
        }

        return render(request, 'account/update.html', context)

@login_required
def requests(request):
    ridesDict = AssignedRender(request.user.id)
    return render(request, 'account/requests.html', ridesDict)
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DetailView
from django.contrib import messages
from .models import Post
from .forms import RiderRequestForm
import logging
from .viewsDbCall import RequestRender, WorkAround, DeleteRequest

#this file renders everything to the screen. When you navigate to a page, you send a request to this file.
#these methods handle those requests. There are a couple of different type of requests, but the main two we will be using are GET and POST
#get is when you request a page, post is when you are trying to send information to that page. 
#the @login_required in front of the methods is a decorator. Decorators take in the entire function as their arguements.
#the reason for this is to do logic before the method is actually called. If an app has a decorators.py file in it, that app as a custom decorator
#look at a decorators.py file for more info (user, driver app has one)
# Create your views here.
@login_required
def rides(request):

    if request.method == 'POST':
        form = RiderRequestForm(request.POST)
        if form.is_valid():
            if WorkAround(form, request):
                
                messages.success(request, f'Request Submitted! Check Request A Ride to view pending requests.')
                return redirect('homepage-home')
            else:
                messages.error(request, f'Uh oh! Looks like something went wrong with filing your request. Try again!')
                return redirect('homepage-home')
    elif request.method == 'GET':
        form = RiderRequestForm()
        
        return render(request, 'request/post_form.html',  {'form': form})
    

@login_required
def welcome(request):
    return render(request, 'request/requestWelcome.html')


def deleteRequest(request, **kwargs):
    if DeleteRequest(kwargs.get('pk')):
        messages.error(request, f'Request Deleted.. Maybe file another one soon ...?')
        return redirect('request-welcome')

@login_required
def viewRides(request):
    requests = RequestRender(request.user.id)

    requestList = {
        'requestList': requests
    
    }
    return render(request, 'request/requestView.html', requestList)


class RequestCreateView(CreateView):
    model = Post
    fields = ['riderLocation', 'destination','date','addSupport']
    

    
    def form_valid(self, form):
        form.instance.rider = self.request.user
        # logging.warning(self.request.user + "Helllllllllllooooooooo")
        return super().form_valid(form)


class RequestDetailView(DetailView):
    model = Post
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users
from .requestDbCall import RequestListRender, AssignedRender, PaymentRender
from request.models import Post
from django.contrib import messages
from .models import AssignedRides
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView
from .assignRide import assignDriver, closeRide, paymentCal
from .forms import CloseRideForm

# Create your views here.
@login_required
@allowed_users(allowed_roles=['admin', 'driver'])
def welcome(request):
    return render(request, 'driver/welcome.html')

@login_required
def rides(request):
    if request.method == 'POST':
        print(request.object)
        return render(request, 'driver/rides.html', request.object)
    elif request.method == 'GET':    
        requestList = RequestListRender()

        return render(request, 'driver/rides.html', requestList)

@login_required
def assignedRides(request):

    context = AssignedRender(request.user.id)
    return render(request, 'driver/assignedRides.html', context)

@login_required
def summary(request):
    return render(request, 'driver/summary.html')


def closeRideView(request, **kwargs):
    
    if request.method == "POST":
        form = CloseRideForm(request.POST)
        if form.is_valid():
            paymentCal(request, form.cleaned_data.get('milage'), kwargs.get("pk"))
            return redirect('driver-welcome')
        
    
    elif request.method == "GET":
        requestObject = closeRide(kwargs.get("pk"))
        renderObjects = {
            "paymentForm": CloseRideForm(),
            "rideObject": requestObject,
        }
        return render(request, 'driver/close_ride.html', renderObjects)


def ridesConfirmation(request):

    

    return render(request, 'driver/rideConfirmation.html')   

def displayPayment(request):

    paymentDict = PaymentRender(request.user)
    return render(request, 'driver/paymentDisplay.html', paymentDict)







class RequestDetailView(DetailView):
    model = Post
    template_name = 'driver/post_detail.html'

    def post(self, request, *args, **kwargs):
        assignDriver(request, kwargs.get("pk"))
        print(kwargs.get("pk"))
        messages.success(request, 'Ride Confirmed!')
        return render(request, 'driver/welcome.html')

class AssignedRequestDetailView(DetailView):
    model = AssignedRides
    template_name = 'driver/assigned_detail.html'

    
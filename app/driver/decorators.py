from django.http import HttpResponse
from django.shortcuts import redirect

#this is a custom decorator. It takes in a function and a list as it's arguements
#the function will be in the views.py and the list will be hard coded there as well
#this decorator checks to see if the user requesting the page is in the correct group to have permission.
#if the user has a group assigned to them, it wil check if that group is allowed in the allowed roles.
#if it is, the wrapper_func returns the function with its arguments and keyword arguements
#if the user is not in the correct group to view the page, it returns an HTTP Response and
#prevents the views.py function from executing. This decorator will check every single time the views.py function is called
def allowed_users(allowed_roles = []):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                 return HttpResponse("You can't views this page")
        return wrapper_func
    return decorator
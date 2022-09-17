from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect, render


# Create your views here.

def home(request):
    return render(request, "Saraswakarma/index.html")



def signup(request):

    if request.method == "POST":
        username = request.POST.get("username")
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myUser = User.objects.create_user(username, email, pass1)
        myUser.first_name = fname;
        myUser.last_name = lname;

        myUser.save()
        messages.success(request, 'Your account has been successfully created')
        return redirect("signin")
    return render(request, "Saraswakarma/signup.html")


def signin(request):

    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']


        user = authenticate(username = username, password = pass1)

        if user is not None:
            login(request, user)
            fname =user.first_name
            return render(request, "Saraswakarma/index.html", {'fname': fname})

        else:
            messages.error(request, "Bad Credentials")
            return redirect('home')
    return render(request, "Saraswakarma/signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('home')

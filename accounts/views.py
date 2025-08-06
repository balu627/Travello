
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth

def destinations(request):
    if request.user.is_authenticated:
        return render(request, "destinations.html")
    else:
        return login(request)

def news(request):
    if request.user.is_authenticated:       
        return render(request, "news.html")
    else:
        return login(request)

def contact(request):
    if request.user.is_authenticated:
        return render(request, "contact.html")
    else:
        return login(request)

def about(request):
    if request.user.is_authenticated:
        return render(request, "about.html")
    else:
        return login(request)

def login(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username,password=password)
    
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"invalid Cred")
            return redirect("login")
    else:
        return render(request, "login.html")


def register(request):
    if request.method == 'POST' :
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        username = request.POST["username"]
        password = request.POST["password1"]
        cpassword = request.POST["password2"]
        email = request.POST["email"]

        if(password == cpassword):
            if(User.objects.filter(username=username).exists()):
                print("Username already exists")
                return redirect('register')
            elif(User.objects.filter(email=email).exists()):
                print("Email already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=firstname, last_name=lastname)
                user.save();
                print("User registered successfully")
                return redirect('login')
        else:
            print("Passwords do not match")
            return redirect('register')
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
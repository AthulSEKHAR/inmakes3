from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['User name']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid")
            return redirect('login')
    return render(request,'login.html')

def register(request):
    if request.method== 'POST':
        username = request.POST['User name']
        Fisrtname = request.POST['First_name']
        Secondname = request.POST['Second_name']
        email = request.POST['Email']
        #mobile = request.POST['Mobile']
        password = request.POST['Password']
        cpassword = request.POST['Password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'user name already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'user name already exists')
                return redirect('register')
            else:
                user= User.objects.create_user(username=username,first_name=Fisrtname,last_name=Secondname,email=email,password=password)
                user.save();
                print("user created")
                return redirect('login')
        else:
            messages.info(request,"password not match")
            return redirect('register')






    return render(request,"project.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
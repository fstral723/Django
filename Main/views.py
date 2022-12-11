from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import User


def index(req):
    return render(req,"Main/index.html")

def profile(req):
    return render(req,"Main/profile.html")

def logout_user(req):
    logout(req)
    return redirect("Main:index")

def signin(req):
    if req.method == "POST":
        un = req.POST.get("uname")
        up = req.POST.get("upass")
        u = authenticate(username=un, password=up)
        if u:
            login(req,u)
            return redirect("Main:index")
        else:
            pass
    
    return render(req,"Main/signin.html")

def signup(req):
    if req.method == "POST":
        un = req.POST.get("uname")
        up = req.POST.get("upass")
        uc = req.POST.get("ucomn")
        pi = req.FILES.get("upic")  
        User.objects.create_user(username=un, password=up, comment=uc, pic=pi)
        return redirect("Main:signin")
    return render(req,"Main/signup.html")

def update(req):
    if req.method == "POST":
        u = req.user
        up = req.POST.get("upass")
        um = req.POST.get("umail")
        pi = req.FILES.get("upic")
        uc = req.POST.get("ucomn")       
        if up:
            u.set_password(up)
        if pi:
            u.pic = pi
        u.comment = uc
        u.email = um
        u.save()
        login(req,u)
        return redirect("Main:profile")
    return render(req,"Main/update.html")

def delete(req):
    req.user.delete()
    return redirect("Main:index")
# Create your views here.

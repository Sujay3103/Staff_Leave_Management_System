from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from accounts.models import Profile
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def homeview(request):
    return render(request,'home.html')

def register(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST["password"]
        role=request.POST["role"]
        user=User.objects.create_user(username=username,password=password)
        Profile.objects.create(user=user,role=role)
        return redirect('login')
    return render(request,'register.html')

def auth(request):
    if request.method=="POST":
        uname=request.POST['username']
        pwd=request.POST['password']
        auth_user=authenticate(request,username=uname,password=pwd)
        if auth_user:
            login(request,auth_user)
            if auth_user.profile.role=="admin":
                return redirect('admin_dash')
            else:
                return redirect('staff_dash')
    return render(request,'login.html')

@login_required
def admin_dash(request):
    if request.user.profile.role !='admin':
        return redirect('staff_dash')
    return render(request,'admin_dashboard.html')

@login_required
def staff_dash(request):
    return render(request,'staff_dashboard.html')

@login_required
def log_out(request):
    logout(request)
    return redirect('home')

@login_required
def manage_staff(request):
    if request.user.profile.role != "admin":
        return redirect('staff_dash')
    staff_det=User.objects.filter(profile__role='staff')
    c={'s_d':staff_det}
    return render(request,'manage_staff.html',c)

@login_required
def add_staff(request):
    if request.user.profile.role != "admin":
        return redirect('staff_dash')
    
    if request.method == "POST":
        uname=request.POST['username']
        pwd=request.POST['password']
        user=User.objects.create_user(username=uname,password=pwd)
        Profile.objects.create(user=user,role="staff")
        return redirect('manage_staff')
    return render(request,'Add_staff.html')

@login_required
def edit_staff(request,id):
    if request.user.profile.role != "admin":
        return redirect('staff_dash')
    user=get_object_or_404(User,id=id)
    if request.method=="POST":
        user.username=request.POST['username']
        user.save()
        return redirect('manage_staff')
    c={'username':user}
    return render(request,'edit_staff.html',c)

@login_required
def delete_staff(request,id):
    if request.user.profile.role != "admin":
        return redirect('staff_dash')
    user=get_object_or_404(User,id=id)
    user.delete()
    return redirect('manage_staff')
    
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from leave.models import Leave

# Create your views here.
@login_required
def apply_leave(request):
    if request.method=="POST":
        Leave.objects.create(
            user=request.user,
            leave_type=request.POST['leave_type'],
            start_date=request.POST['start'],
            end_date=request.POST['end'],
            reason=request.POST['reason'],
            status='Pending'
        )
        return redirect('staff_dash')
    return render(request,'apply_leave.html')

@login_required
def my_leaves(request):
    leaves=Leave.objects.filter(user=request.user)
    return render(request,"my_leaves.html",{'leaves':leaves})

@login_required
def view_leave(request):
    if request.user.profile.role !="admin":
        return redirect('staff_dash')
    lev=Leave.objects.all()
    return render(request,'view_leaves.html',{'leave':lev})

@login_required
def approve_leave(request,id):
    if request.user.profile.role != 'admin':
        return redirect('staff_dash')
    data=get_object_or_404(Leave,id=id)
    data.status="Approved"
    data.save()
    return redirect('view_leave')

@login_required
def reject_leave(request,id):
    if request.user.profile.role != 'admin':
        return redirect('staff_dash')
    data=get_object_or_404(Leave,id=id)
    data.status="Rejected"
    data.save()
    return redirect('view_leave')
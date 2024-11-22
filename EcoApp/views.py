from django.contrib import messages, auth
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from EcoApp.forms import UserRegister, customerform, dealerform


# Create your views here.

def indexpage(request):
    return render(request,'index.html')

def loginpage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=auth.authenticate(username=username, password=password)
        if user is not None and user.is_staff:
            login(request,user)
            return redirect('adminpage')
        elif user is not None and user.is_customer:
            if user.customer.approval_status==1:
                login(request,user)
                return redirect('base')
            else:
                messages.info(request,"Your Are Not Approved To Login")
        elif user is not None and user.is_dealer:
            if user.dealer.approval_status==1:
                login(request,user)
                return redirect('dealerwelcomepage')
            else:
                messages.info(request,"Your Are Not Approved To Login")
        elif user is not None and user.is_authority:
            login(request,user)
            return redirect('authoritypage')
        else:
            messages.info(request, "Not Registered User")
    return render(request,'login.html')

def reg_drop(request):
    return render(request,'regdrop.html')

def user_reg(request):
    u_form = UserRegister()
    c_form = customerform()
    if request.method == 'POST':
        u_form = UserRegister(request.POST)
        c_form = customerform(request.POST, request.FILES)
        if u_form.is_valid() and c_form.is_valid():
            user = u_form.save(commit=False)
            user.is_customer = True
            user.save()
            customer = c_form.save(commit=False)
            customer.user = user
            customer.save()
            messages.info(request, "customer registered successfully")
            return redirect('loginpage')
    return render(request,'user_reg.html',{'u_form':u_form,'c_form':c_form})

def dealer_reg(request):
    u_form = UserRegister()
    d_form = dealerform()
    if request.method == 'POST':
        u_form = UserRegister(request.POST)
        d_form = dealerform(request.POST, request.FILES)
        if u_form.is_valid() and d_form.is_valid():
            user = u_form.save(commit=False)
            user.is_dealer = True
            user.save()
            dealer = d_form.save(commit=False)
            dealer.user = user
            dealer.save()
            messages.info(request, "dealer registered successfully")
            return redirect('loginpage')
    return render(request,'dealer_reg.html',{'u_form':u_form,'d_form':d_form})

def authority(request):
    return render(request,'authority_reg.html')

def adminpage(request):
    return render(request,'adminpage.html')

def base(request):
    return render(request,'base.html')
def customepage(request):
    return render(request,'customepage.html')

def dealerpage(request):
    return render(request,'dealerpage.html')

def dealerwelcomepage(request):
    return render(request,'dealer_welcome.html')

def authoritypage(request):
    return render(request,'authoritypage.html')

def log_out(request):
    logout(request)
    return redirect('indexpage')

from django.contrib import messages
from django.shortcuts import render, redirect

from EcoApp.forms import UserRegister, authorityform
from EcoApp.models import Customer, Dealer, Authority, Scrap


def view_cus(request):
    data=Customer.objects.all()
    return render(request,'view_cus.html',{'data':data})

def view_dealer(request):
    data=Dealer.objects.all()
    return render(request,'view_dealer.html',{'data':data})

def tap_authority(request):
    return render(request,'tap_authority.html')

def add_authority(request):
    u_form = UserRegister()
    e_form = authorityform()
    if request.method == 'POST':
        u_form = UserRegister(request.POST)
        e_form = authorityform(request.POST, request.FILES)
        if u_form.is_valid() and e_form.is_valid():
            user = u_form.save(commit=False)
            user.is_authority = True
            user.save()
            authority = e_form.save(commit=False)
            authority.user = user
            authority.save()
            messages.info(request, "authority registered successfully")
            return redirect('tap_authority')
    return render(request,'add_authority.html',{'u_form':u_form,'e_form':e_form})

def view_authority(request):
    data=Authority.objects.all()
    return render(request,'view_authority.html',{'data':data})

def approve_customer(request,id):
    customer=Customer.objects.get(user_id=id)
    customer.approval_status=1
    customer.save()
    messages.info(request,'customer approved successfully')
    return redirect('view_cus')

def reject_customer(request,id):
    data1 = Customer.objects.get(user_id=id)
    data = Customer.objects.get(user=data1)
    if request.method == 'POST':
        data.delete()
        return redirect('view_cus')
    else:
        return redirect('view_cus')

def approve_dealer(request,id):
    dealer=Dealer.objects.get(user_id=id)
    dealer.approval_status=1
    dealer.save()
    messages.info(request,'dealer approved successfully')
    return redirect('view_dealer')

def reject_dealer(request,id):
    data1 = Dealer.objects.get(user_id=id)
    data = Dealer.objects.get(user=data1)
    if request.method == 'POST':
        data.delete()
        return redirect('view_dealer')
    else:
        return redirect('view_dealer')

def ad_view(request):
    data=Scrap.objects.all()
    return render(request,'ad_view.html',{'data':data})

def reject_ad(request,id):
    data1 = Scrap.objects.get(id=id)
    data = Scrap.objects.get(user=data1)
    if request.method == 'POST':
        data.delete()
        return redirect('ad_view')
    else:
        return redirect('ad_view')

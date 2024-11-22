from django.contrib import messages
from django.shortcuts import render, redirect

from EcoApp.models import Scrap


def view_ads_au(request):
    data=Scrap.objects.all()
    return render(request,'view_ads_au.html',{'data':data})

def approve_ad(request,id):
    scrap=Scrap.objects.get(id=id)
    scrap.approval_status=1
    scrap.save()
    messages.info(request,'Ads approved successfully')
    return redirect('view_ads_au')
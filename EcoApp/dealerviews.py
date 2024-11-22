from django.shortcuts import render

from EcoApp.models import Scrap


def ads(request):
    data=Scrap.objects.all()
    return render(request,'ads.html',{'data':data})
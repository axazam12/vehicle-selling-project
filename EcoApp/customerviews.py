from django.contrib import messages
from django.shortcuts import redirect, render

from EcoApp.forms import Scrapform
from EcoApp.models import Customer, Scrap


def scrapadd(request):
    c=Customer.objects.get(user=request.user)
    form=Scrapform()
    if request.method == 'POST':
        form=Scrapform(request.POST,request.FILES)
        f=form.save(commit=False)
        f.customer = c
        f.save()
        messages.info(request,'Your scrap added successfully')
        return redirect('customepage')
    return render(request,'add_scrap.html',{'form':form})

def scrap_view(request):
    data=Scrap.objects.all()
    return render(request,'scrap_view.html',{'data':data})
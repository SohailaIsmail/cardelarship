from django.shortcuts import render
from .models import Car

def products(request):  #read function
    return render(request,'product/all.html',  {'pro':Car.objects.all()})

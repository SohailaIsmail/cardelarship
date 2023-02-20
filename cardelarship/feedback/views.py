from django.shortcuts import render
from .models import feed
from pages.models import signUp


def feedbacks(request):
    if request.method=='POST':
        txt=request.POST.get('feed')
        feedobj=feed()
        feedobj.feedback=txt
        feedobj.name=signUp.name
        feedobj.save()
    return render(request,'feedback/feed.html')


def allfeedbacks(request):
    return render(request,'feedback/feedbacks.html',  {'feed':feed.objects.all()})

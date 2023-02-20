from django.shortcuts import render
from django.http import HttpResponse
from .models import signUp ,LogIn

def home(request):
    return render(request , 'pages/home.html')

def signup(request):
    NAME = request.POST.get('Name')
    USERNAME = request.POST.get('Username')
    PASSWORD= request.POST.get('Password')
    EMAIL = request.POST.get('Email')
    data =signUp(name=NAME  , username=USERNAME  , password=PASSWORD , email=EMAIL )
    if request.method == 'POST':
        data.save()
    return render(request , 'pages/signup.html' )

def log(request):
    USERNAME = request.POST.get('username')
    PASSWORD= request.POST.get('Pass')
    data =LogIn(username=USERNAME  , password=PASSWORD)
    if request.method == 'POST':
        data.save()
    return render(request , 'pages/login.html' )

def contact(request):
        if request.method=='GET':
            return render(request , 'footer.html')



def createinfo(request):
    NAME = request.POST['Name']
    USERNAME = request.POST.get('Username')
    PASSWORD= request.POST.get('Password')
    EMAIL = request.POST.get('Email')
    data =signUp(name=NAME  , username=USERNAME  , password=PASSWORD , email=EMAIL )
    if request.method == 'POST':
        data.save()
    return HttpResponse('successfully created')


def updatename(request):
    NAME = request.POST.get(instance = 'name')
    signUp.name= NAME
    if request.method == 'POST':
        signUp.name.save()
    return HttpResponse('successfully update')


def deleteinfo(request, id ):
    info = request.POST.get(id=id)
    if request.method == 'POST':
        info.delete()
    return HttpResponse('successfully deleted')
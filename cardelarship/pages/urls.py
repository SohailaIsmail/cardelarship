from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    
    path('home/',views.home ),
    path('content/',views.contact),
    path('SignUp/',views.signup),
    path('LoGin/',views.log),
    
]

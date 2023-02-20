from django.urls import path
from . import views


urlpatterns = [

    path('', views.feedbacks, name='feedback'),
    path('allfeedbacks/', views.allfeedbacks, name='feedback'),

]

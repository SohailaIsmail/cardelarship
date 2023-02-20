from django.db import models

class signUp(models.Model): 
    name = models.CharField(max_length=70) 
    username = models.CharField( max_length=70)
    password = models.CharField( max_length=70)
    email = models.CharField(max_length=70)
    def __str__(self):
            return self.name
    
    class Meta:
        verbose_name ='usersinfo'

class LogIn(models.Model): 
    username = models.CharField( max_length=70)
    password = models.CharField( max_length=70)
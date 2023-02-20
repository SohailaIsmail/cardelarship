from unicodedata import decimal
from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=50)
    carmodel = models.CharField(max_length=20)
    content=models.TextField(max_length=300)
    price=models.DecimalField(max_digits =50 , decimal_places = 3 )
    active=models.BooleanField(default=True)
    c_image=models.ImageField(upload_to='photos/%y/%m/%d')

    def __str__(self):
        return self.name
    

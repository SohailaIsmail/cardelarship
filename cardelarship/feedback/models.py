
from pages.models import signUp
from django.db import models

class feed(models.Model):
    
    feedback = models.CharField(max_length=20)
    signUp = models.ForeignKey(signUp, null=True , on_delete=models.CASCADE , related_name="feedbacks")

  
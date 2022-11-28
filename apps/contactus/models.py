from django.db import models
from django.contrib.auth.models import User

class Contact_us_model(models.Model):

    fullname=models.CharField(max_length=30)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=12)
    CHOICES=[('acc','Account'),('sup','Supply'),('prd','Products'),('web','Website_issue'),('ord','Order'),('pay','Payment')]
    category=models.CharField(max_length=20,choices=CHOICES)
    description=models.TextField()
    registered=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.description}"


from django.db import models
from django.db.models.base import Model

# Create your models here.

class Customer(models.Model):
    name= models.CharField(max_length=100)
    email= models.EmailField(max_length=100)
    phone= models.CharField(max_length=100)
    city= models.CharField(max_length=100)
    current_balance= models.IntegerField()

class Transaction(models.Model):
    sender_id=models.CharField(max_length=100)
    sender_name=models.CharField(max_length=100)
    receiver_id=models.CharField(max_length=100)
    receiver_name=models.CharField(max_length=100)
    Amount=models.CharField(max_length=10)

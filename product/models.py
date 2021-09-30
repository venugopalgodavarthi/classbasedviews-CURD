from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import *
from django.db.models.fields.related import ForeignKey

# Create your models here.
class itemmodel(models.Model):
    itemname=models.CharField(max_length=20)

class productmodel(models.Model):
    pname =models.CharField(max_length=30)
    pdesc =models.CharField(max_length=50)
    price = models.FloatField()
    discount=models.FloatField()
    item= models.ForeignKey(itemmodel,on_delete=CASCADE)
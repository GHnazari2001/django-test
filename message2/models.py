from django.db import models

# Create your models here.
class message2(models.Model):
    text= models.CharField(max_length=255)
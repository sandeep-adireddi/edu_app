from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Test_Data(models.Model):
   id = models.primary_key=True
   name = models.CharField(max_length = 50)
   age = models.IntegerField()
   gender = models.CharField(max_length = 50)
   score = models.IntegerField()
   subject = models.CharField(max_length = 150)
   region = models.CharField(max_length = 50)



class Users_Data(models.Model):
   id = models.primary_key=True
   name = models.CharField(max_length = 150)
   user = models.CharField(max_length = 50)
   email = models.CharField(max_length = 50)
   password = models.CharField(max_length = 50)
   auth = models.BooleanField(default=False)




class Notify_Data(models.Model):
   id = models.primary_key=True
   from_user = models.CharField(max_length = 150)
   to_user = models.CharField(max_length = 150)
   comment = models.CharField(max_length = 50)
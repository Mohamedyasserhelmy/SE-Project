from django.db import models

class User(models.Model):
    #ID IS auto-generated
    #models is tested
    customer = 'customer' 
    username = models.CharField(max_length=30, blank = False, null = False)
    email = models.EmailField(max_length=40, blank = False, null = False)
    password = models.CharField(max_length=20, blank = False, null = False)
    address = models.CharField(max_length=30, blank = False, null = False)
    Type = models.CharField(max_length = 15, blank = False, null = False, default= customer)

from django.db import models
from django.utils import timezone
import uuid

class Driver(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=True,null=True)
    
    def __str__(self):
        return self.name

class Client(models.Model):
    client_name = models.CharField(null=True,max_length=255)
    created = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=True,null=True)
    
    def __str__(self):
        return self.client_name

class Order(models.Model):

    STATUS_CHOICES = (
        ('CREATED','Created'),
        ('ACCEPTED','Accepted '),
        ('CANCELLED','Cancelled'),
        ('FINISHED','Finished'),
    )
    driver = models.ForeignKey(Driver,on_delete=models.CASCADE,related_name='driver')
    client = models.ForeignKey(Client,on_delete=models.CASCADE,related_name='client')
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='CREATED')
    updated = models.DateTimeField(auto_now=True,null=True)
    created_day = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"This order status is {self.status} driver name is {self.driver} and client name is {self.client}"
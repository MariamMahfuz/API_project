# from email import message
from django.db import models

# Create your models here.
class Message(models.Model):
    name=models.CharField(max_length=60)
    address=models.CharField(max_length=300)
    message=models.CharField(max_length=500)
    def __str__(self):
        return str(self.name)
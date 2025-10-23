from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publish = models.DateField(auto_now=True)
    Category = models.CharField(max_length=200)
    in_stock = models.CharField(max_length=20)
    
    
    class Meta:
        def __str__(self):
            return self.id
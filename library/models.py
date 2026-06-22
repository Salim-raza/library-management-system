from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    Category = models.CharField(max_length=200)
    in_stock = models.CharField(max_length=20)
    publish = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        def __str__(self):
            return self.id

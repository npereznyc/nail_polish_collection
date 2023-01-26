from django.db import models

# Create your models here.
class Brands(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class Polishes(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=400)
    brand = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['brand', 'name'] 

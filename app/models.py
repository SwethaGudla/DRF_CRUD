from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=30)
    age= models.IntegerField()
    domain = models.CharField(max_length=30)
    
    
    def __str__(self):
        return self.name

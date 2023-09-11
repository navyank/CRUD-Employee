from django.db import models

# Create your models here.
class Position(models.Model):
    title=models.CharField(max_length=100)
    def __str__(self):
        return self.title
class Employee(models.Model):
    Fullname=models.CharField(max_length=100)
    Empcode=models.CharField(max_length=100)  
    Mobile=models.CharField(max_length=100)
    position=models.ForeignKey(Position,on_delete=models.CASCADE)  
    
    def __str__(self):
        return self.Fullname
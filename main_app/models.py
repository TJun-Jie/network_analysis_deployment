from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length =128)

    def __str__(self):
        return self.name
    

class Friendship1(models.Model):
    student = models.ForeignKey(Student,related_name="student",on_delete=models.CASCADE)
    friend = models.ForeignKey(Student,related_name="friend",on_delete=models.CASCADE)


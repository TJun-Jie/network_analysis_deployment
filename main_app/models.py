from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length =128)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "student_table"

class Friendship1(models.Model):
    student = models.ForeignKey(Student,related_name="student",on_delete=models.CASCADE)
    friend = models.ForeignKey(Student,related_name="friend",on_delete=models.CASCADE)

    class Meta:
        db_table = "friendship_table"
    
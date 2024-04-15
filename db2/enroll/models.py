from django.db import models

# Create your models here.

class Student(models.Model):
    stuRoll=models.IntegerField()
    stuName=models.CharField(max_length=70)
    stuEmail=models.CharField(max_length=70)
    stuDOB=models.DateField()

    def __str__(self):
        return self.stuName
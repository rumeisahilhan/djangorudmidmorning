from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=30,blank=False,null=False)
    email=models.EmailField()
    age=models.IntegerField()
    gender=models.CharField(max_length=30,blank=False,null=False)
def __dir__(self):
    return self.name
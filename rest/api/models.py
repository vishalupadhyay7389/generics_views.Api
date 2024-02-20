from django.db import models
from rest_framework import serializers
from django.core.validators import MinLengthValidator , RegexValidator

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    
    def __str__(self):
        return self.name
class Student(models.Model):
    name = models.CharField(max_length=120)
    age = models.CharField(max_length=120)
    phone = models.CharField(max_length=120 , validators= [MinLengthValidator(10,message="Mobile number Must be at least at 10 digit long."),RegexValidator(r'^9\d{9}$',message="Mobile number must start with 9 and be 10 digit long .")])
    address = models.CharField(max_length=120)
    school = models.ForeignKey(School , on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
class StudentSerlizer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

from django.db import models

# Create your models here.
class User(models.Model):
    ROLL_NUM = models.AutoField(primary_key=True)
    Company_Name = models.CharField(max_length=255)
    Job_Role = models.CharField(max_length=255)
    DateofInterview = models.DateField()  # Change from CharField to DateField
    TimeofInterview = models.TimeField()  # Change from CharField to TimeField
    Address = models.TextField()

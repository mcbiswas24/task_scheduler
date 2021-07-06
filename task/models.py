from django.db import models
from authentication.models import User_Table

# Create your models here.

class Task_Details(models.Model):
    Email = models.ForeignKey(User_Table, on_delete=models.CASCADE)
    TaskName = models.CharField(max_length = 50)
    TaskDescription = models.CharField(max_length = 150)
    Priority = models.CharField(max_length = 2)
    StartDate = models.DateField()
    EndDate = models.DateField()
    Day = models.CharField(max_length = 10, default = 0)

    def __str__(self):
        return '%s' % (self.Email)

from django.db import models

# Create your models here.

class User_Table(models.Model):
    FirstName = models.CharField(max_length = 50)
    LastName = models.CharField(max_length = 50)
    Email = models.EmailField(primary_key= True)
    Password = models.CharField(max_length = 20)

    def __str__(self):
        return '%s' % (self.Email)
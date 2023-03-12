from django.db import models

class Students(models.Model):
    sname = models.CharField(max_length=50)
    age = models.CharField(max_length=3)
    email = models.CharField(max_length=50)
   
    def __str__(self):
        return self.sname

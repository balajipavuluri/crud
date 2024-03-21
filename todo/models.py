from django.db import models

# Create your models here.

class Contactinfo(models.Model):
    name=models.CharField(max_length=255)
    number = models.IntegerField()

    def __str__(self):
        return self.name+ "   " + str(self.number)  

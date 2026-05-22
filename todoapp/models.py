from django.db import models

# Create your models here.
class table(models.Model):
    task = models.CharField(max_length=100)
    date= models.DateField()
    



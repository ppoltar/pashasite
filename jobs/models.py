from django.db import models


# Create your models here.
class Job(models.Model):

    image = models.ImageField(upload_to='images/')

    title  = models.CharField(max_length=100)

    description1 = models.CharField(max_length = 5000)
    description2 = models.CharField(max_length = 5000 ,blank=True)
    description3 = models.CharField(max_length = 5000 ,blank=True)
    description4 = models.CharField(max_length=5000, blank=True)
    description5 = models.CharField(max_length=5000, blank=True)
    description6 = models.CharField(max_length=5000, blank=True)
    description7 = models.CharField(max_length=5000, blank=True)
    description8 = models.CharField(max_length=5000, blank=True)
    #description =  models.TextField(max_length = 5000)



    def __str__(self):
        return self.title

class Education(models.Model):

    image = models.ImageField(upload_to='images/')
    title  = models.CharField(max_length=100)
    description = models.CharField(max_length = 5000)
    address = models.CharField(max_length=200)

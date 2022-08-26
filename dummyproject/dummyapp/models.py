from django.db import models

# Create your models here.

class place(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return self.name

class human(models.Model):
    name1 = models.CharField(max_length=100)
    image1 = models.ImageField()
    description1 = models.TextField()

    def __str__(self):
        return self.name1
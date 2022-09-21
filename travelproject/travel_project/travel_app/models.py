from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name

class Team(models.Model):
    Name1=models.CharField(max_length=250)
    Img1=models.ImageField(upload_to='pics')
    Desc1=models.TextField()

    def __str__(self):
        return self.Name1

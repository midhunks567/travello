from django.db import models

# Create your models here.

class place(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='picture')
    desc=models.TextField()
    price=models.IntegerField()
    offers=models.BooleanField(default=False)

class news(models.Model):
    date=models.DateField()
    img=models.ImageField(upload_to='picture')
    cap=models.TextField()
    desc=models.TextField()

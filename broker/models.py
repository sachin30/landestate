from django.db import models

# Create your models here.
class Broker(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    phone=models.IntegerField()
    photo=models.ImageField(upload_to="")
    
    def __str__(self):
        return self.first_name
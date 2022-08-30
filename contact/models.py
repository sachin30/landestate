from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=50)
    phone=models.CharField(max_length=12)
    message=models.TextField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        #verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
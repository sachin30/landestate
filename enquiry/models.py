from django.db import models
from property.models import Property

# Create your models here.

class Enquiry(models.Model):
    property_enquired=models.ForeignKey(Property,on_delete=models.CASCADE)
    visitor_name=models.CharField(max_length=50)
    visitor_email=models.EmailField()
    visitor_phone=models.CharField(max_length=12)

    class Meta:
        verbose_name = 'Enquiry'
        verbose_name_plural = 'Enquiries'
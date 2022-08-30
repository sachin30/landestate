from django.db import models
from broker.models import Broker
from ckeditor.fields import RichTextField

# Create your models here.
class Property(models.Model):
    BEDROOM_CHOICES=(
        ("1","1"),
        ("2","2"),
        ("3","3"),
    )

    broker=models.ForeignKey(Broker, on_delete=models.DO_NOTHING)
    title=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zipcode=models.IntegerField()
    description=RichTextField()#ckeditor field for admin panel
    price=models.IntegerField()
    bedrooms=models.CharField(max_length=2,choices=BEDROOM_CHOICES,blank=True,null=True)
    bathrooms=models.CharField(max_length=2,choices=BEDROOM_CHOICES,blank=True,null=True)
    garage=models.IntegerField()
    sqft=models.IntegerField()
    plot_size=models.IntegerField()
    photo_main=models.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True)
    photo_2=models.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True)
    photo_3=models.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True)
    photo_4=models.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True)
    photo_5=models.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True)
    
    slug=models.SlugField(max_length=200)

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

    def __str__(self):
        return self.title
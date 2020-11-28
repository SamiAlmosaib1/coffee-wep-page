from django.db import models
from django.db.models.fields import TextField
from django.db.models.fields.files import ImageField
from datetime import datetime

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    
    price=models.DecimalField(max_digits=5, decimal_places=2)
    photo=models.ImageField(upload_to='photo/%Y/%m/%d/')
    is_active=models.BooleanField(default=True)
    publish_date=models.DateTimeField(default=datetime.now)
     

    def __str__(self):
        return self.name

    class Meta:
        ordering=['publish_date']

from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    img =models.ImageField(upload_to='pics')
    img_type = models.CharField(max_length=50)


    def __str__(self):
        return self.name
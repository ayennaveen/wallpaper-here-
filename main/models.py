from django.db import models
from cloudinary.models import CloudinaryField

class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = CloudinaryField('image')
    img_type = models.CharField(max_length=50)

    def __str__(self):
        return self.name

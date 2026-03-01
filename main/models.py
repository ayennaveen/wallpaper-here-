from django.db import models

class Wallpaper(models.Model):

    DEVICE_CHOICES = [
        ('mobile', 'Mobile'),
        ('desktop', 'Desktop'),
    ]

    TYPE_CHOICES = [
        ('anime', 'Anime'),
        ('nature', 'Nature'),
        ('mountain', 'Mountain'),
        ('games', 'Games'),
    ]

    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='wallpapers/')
    device = models.CharField(
        max_length=10,
        choices=DEVICE_CHOICES,
        default='mobile'
    )
    type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        default='nature'
    )

    def __str__(self):
        return self.title
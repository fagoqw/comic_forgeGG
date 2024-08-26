from django.db import models
from django.contrib.auth.models import User


class Comic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='comic_covers/')
    images = models.ManyToManyField('ComicImage', blank=True)

    def __str__(self):
        return self.title


class ComicImage(models.Model):
    image = models.ImageField(upload_to='comic_images/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.description or 'No description'

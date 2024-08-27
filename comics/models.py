from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Comic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='comic_covers/')
    description = models.TextField(blank=True, null=True)
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ComicImage(models.Model):
    comic = models.ForeignKey(Comic, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='comic_images/')
    description = models.TextField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.description or 'No description'



class Comment(models.Model):
    comic = models.ForeignKey(Comic, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.comic.title}'

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

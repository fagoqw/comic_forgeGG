from django.db import models
from django.contrib.auth.models import User
from comics.models import Comic


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True, default='avatars/default_avatar.png')
    follows = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='followed_by')

    def __str__(self):
        return self.user.username

    def created_comics(self):
        return Comic.objects.filter(user=self.user)

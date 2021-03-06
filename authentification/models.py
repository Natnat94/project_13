from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image


class User(AbstractUser):
    username = models.EmailField(max_length=254, unique=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', verbose_name='')
    geom = models.PointField(null=True)
    first_name = models.CharField(max_length=25, blank=True)
    last_name = models.CharField(max_length=25, blank=True)
    gender = models.CharField(max_length=6, blank=True)
    friends = models.ManyToManyField("User", related_name="is_friend_with")
    phone = models.CharField(max_length=10, blank=True)
    is_confirmed = models.BooleanField(default=False)
    REQUIRED_FIELDS = []
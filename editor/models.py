from django.db import models

# Create your models here.

class Pose(models.Model):
    register_date = models.DateTimeField(auto_now=True)
    english_name = models.CharField(max_length=256)
    pose_image = models.ImageField(upload_to='pose_images')

class Sequence(models.Model):
    name = models.CharField(max_length=256)
    register_date = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=256)


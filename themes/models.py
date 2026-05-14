from django.db import models
class Sitesetting(models.Model):
    banner=models.ImageField(upload_to='media/site/')
    caption=models.TextField()
# Create your models here.

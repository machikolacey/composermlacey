from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.

class Advert(models.Model):
    link_url = models.URLField(max_length=1024, null=True, blank=True)
    banner = models.ImageField(null=True, blank=True)
    banner_tablet_size = models.ImageField(null=True, blank=True)
    banner_mobile_size = models.ImageField(null=True, blank=True)    
    name = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.name



class homepageVideo(models.Model):

    title = models.CharField(max_length=254)
    subtitle = models.CharField(max_length=254)
    embed = EmbedVideoField(null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    
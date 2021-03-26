from django.db import models


# Create your models here.


class Advert(models.Model):
    link_url = models.URLField(max_length=1024, default='',  blank=True)
    banner = models.ImageField(default='',  blank=True)
    banner_tablet_size = models.ImageField(default='',  blank=True)
    banner_mobile_size = models.ImageField(default='',  blank=True)
    name = models.TextField(default='',  blank=True)

    def __str__(self):
        return self.name


class homepageVideo(models.Model):

    title = models.CharField(max_length=254)
    subtitle = models.CharField(max_length=254)
    youtube_link = models.CharField(max_length=254, default='',  blank=True)
    details = models.TextField(default='',  blank=True)
    recorded = models.CharField(max_length=254, default='',  blank=True)

    def __str__(self):
        return self.title

from django.db import models


# Create your models here.
class Page(models.Model):

    permalink = models.CharField(max_length=254)
    title = models.CharField(max_length=254)
    content = models.TextField(default='',  blank=True)
    primaryImage = models.ImageField(default='',  blank=True)
    secondaryImage = models.ImageField(default='',  blank=True)

    def __str__(self):
        return self.title


class SampleVideo(models.Model):

    title = models.CharField(max_length=254)
    subtitle = models.CharField(max_length=254)
    youtube_link = models.CharField(max_length=254, default='',  blank=True)
    recorded = models.CharField(max_length=254, default='',  blank=True)
    details = models.TextField(default='',  blank=True)

    def __str__(self):
        return self.title


class Images(models.Model):

    page  = models.ForeignKey('Page', 
            default='', blank=True, on_delete=models.CASCADE)
    image = models.ImageField(default='',  blank=True)
    caption = models.CharField(max_length=254, default='')

    def __str__(self):
        return self.caption

from django.db import models

# Create your models here.
class Page(models.Model):

    permalink = models.CharField(max_length=254)
    title = models.CharField(max_length=254)
    content = models.TextField(null=True, blank=True)
    primaryImage = models.ImageField(null=True, blank=True)
    secondaryImage = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

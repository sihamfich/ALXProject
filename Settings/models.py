from django.db import models

# Create your models here.
class Settings(models.Model):
    site_name = models.CharField(max_length=100)
    site_logo = models.ImageField(upload_to='Settings/')
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    descreption = models.TextField(max_length=300)
    FB_link = models.URLField(max_length=200)
    Twitter_link = models.URLField(max_length=200)
    Instagram_link = models.URLField(max_length=200)
    address = models.TextField(max_length=200)
    
    def __str__(self):
        return self.site_name

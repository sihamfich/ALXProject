from django.db import models

# Create your models here.
class About(models.Model):
    service_overview = models.TextField(max_length=1000)
    our_mission = models.TextField(max_length=1000)
    our_vision = models.TextField(max_length=1000)
    photo = models.ImageField(upload_to='About/')
    
    def __str__(self):
        return str(self.id)
    
class FAQ(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=3000)
    
    def __str__(self):
        return self.name
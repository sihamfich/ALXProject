from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
# Property Model
class Property(models.Model):
    Name = models.CharField(max_length=100)
    Main_Image = models.ImageField(upload_to='Property/')
    Price = models.IntegerField(default=0)
    Description = models.TextField(max_length=10000)
    Location = models.ForeignKey('Location', related_name='Property_Location',on_delete=models.CASCADE)
    Category = models.ForeignKey('Category', related_name='Property_Category',on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Name)
        super(Property, self).save(*args, **kwargs)
      

    # Property Features
    def __str__(self):
        return self.Name
    
    def get_absolute_url(self):
        return reverse("Property:property_detail", kwargs={'slug': self.slug})

# Property Images Model
class PropertyImages(models.Model):
    Property = models.ForeignKey(Property, related_name='Property_Images',on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='Property_Images/')

    def __str__(self):
        return str(self.Property)
    

class Location(models.Model):
    Name = models.CharField(max_length=50)
    Image = models.ImageField(upload_to='Location/')

    def __str__(self):
        return self.Name


class Category(models.Model):
    Name = models.CharField(max_length=40)

    def __str__(self):
        return self.Name
    
class PropertyReview(models.Model):
    
    Author = models.ForeignKey(User, related_name='Review_Auther', on_delete=models.CASCADE)
    Property = models.ForeignKey(Property, related_name='Property_Review', on_delete=models.CASCADE)
    Rating = models.PositiveIntegerField(default=0 ,  validators=[MaxValueValidator(5)])
    Feedback = models.TextField(max_length=2000)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.Property)
    
Count = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
)

class PropertyBooking(models.Model):
    User = models.ForeignKey(User, related_name='Booking_User', on_delete=models.CASCADE)
    Property = models.ForeignKey(Property, related_name='Property_Booking', on_delete=models.CASCADE)
    DateIn = models.DateField(default=timezone.now)
    DateOut = models.DateField(default=timezone.now)
    Guests = models.CharField(max_length=2, choices=Count)
    Children = models.CharField(max_length=2, choices=Count)

    def __str__(self):
        return str(self.Property)   
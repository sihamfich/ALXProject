from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

# Create your models here.

class BlogPost(models.Model):

    Title = models.CharField(max_length=100 , verbose_name=_('Title'))
    Description = models.TextField(max_length=10000 , verbose_name=_('Description'))
    Tags = TaggableManager(_('Tags') ,blank=True)
    Author = models.ForeignKey(User,related_name='BlogPost_author' , on_delete=models.CASCADE , verbose_name=_('Author'))
    CreatedDate = models.DateTimeField(default=timezone.now)
    Image = models.ImageField(_('Image') ,upload_to='BlogPost/')
    Category = models.ForeignKey('Category', related_name='BlogPost_Category', on_delete=models.CASCADE , verbose_name=_('Category'))
    slug = models.SlugField(null=True, blank=True)
   
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Title)
        super(BlogPost, self).save(*args, **kwargs) # Call the real save() method

 
    def __str__(self):
        return self.Title
    
    def get_absolute_url(self):
        return reverse("Blog:blogpost_Detail", kwargs={"slug": self.slug})
    

class Category(models.Model):
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name
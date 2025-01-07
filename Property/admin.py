from django.contrib import admin

# Register your models here.
from .models import Property , PropertyImages , Location , Category , PropertyReview , PropertyBooking

admin.site.register(Property)
admin.site.register(PropertyImages)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(PropertyReview)
admin.site.register(PropertyBooking)

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from .models import Property , PropertyImages , Location , Category , PropertyReview , PropertyBooking


# Apply summernote to all TextField in model.
class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display = ['Name','Price','get_avg_rating','check_availability']




admin.site.register(Property, SomeModelAdmin)
admin.site.register(PropertyImages)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(PropertyReview)
admin.site.register(PropertyBooking)

from django import forms

from .models import PropertyBooking , PropertyReview


class PropertyBookingForm(forms.ModelForm):
       
    class Meta:
        model = PropertyBooking
        fields = ['DateIn','DateOut', 'Guests', 'Children']
       

class PropertyReviewForm(forms.ModelForm):
    class Meta:
        model = PropertyReview
        fields = ['Rating','Feedback']

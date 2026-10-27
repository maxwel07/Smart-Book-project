from django import forms
from .models import Reviews, Service, Booking


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['customer_name', 'rating', 'comment']

        def clean_rating(self):
            rating = self.cleaned_data['rating']

            if rating < 1 or rating > 5:
                raise forms.ValidationError("Rating must be between 1 and 5.")

            return rating

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['service', 'appointment_date', 'start_time']

        widgets = {
            'appointment_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'start_time': forms.TimeInput(
                attrs={'type': 'time'}
            ),
        }

    def __init__(self, *args, business=None, **kwargs):
        super().__init__(*args, **kwargs)

        if business is not None:
            self.fields['service'].queryset = Service.objects.filter(
                business=business,
                is_active=True
            )
        else:
            self.fields['service'].queryset = Service.objects.none()



    

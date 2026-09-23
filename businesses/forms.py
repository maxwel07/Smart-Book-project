from django import forms
from .models import Reviews

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['customer_name', 'rating', 'comment']

        def clean_rating(self):
            rating = self.cleaned_data['rating']

            if rating < 1 or rating > 5:
                raise forms.ValidationError("Rating must be between 1 and 5.")

            return rating

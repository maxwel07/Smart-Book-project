from django import forms
<<<<<<< HEAD
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['customer_name', 'rating', 'comment']
=======
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
>>>>>>> 98bcece778846efd2d4b61364bb38fdb7dcdc270

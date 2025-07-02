
from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """ __init logic from chatGPT to display product name on dropdown """
    class Meta:
        model = Review
        fields = ['product', 'comments', 'rating']
        
    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating < 1 or rating > 5:
            raise forms.ValidationError("Rating must be between 1 and 5.")
        return rating

        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].label_from_instance = lambda obj: obj.name
        self.fields['rating'].help_text = "Please rate between 1 and 5 only."


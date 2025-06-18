
from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """ __init logic from chatGPT to display product name on dropdown """
    class Meta:
        model = Review
        fields = ['product', 'comments', 'rating']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].label_from_instance = lambda obj: obj.name

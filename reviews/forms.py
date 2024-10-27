from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(attrs={
                'class': 'border border-gray-300 rounded-lg p-2 w-full',
                'placeholder': 'Select a rating'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'border border-gray-300 rounded-lg p-2 w-full',
                'rows': 4,
                'placeholder': 'Leave your comment here'
            }),
        }

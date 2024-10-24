from restaurants.models import Restaurant
from django import forms
from django.utils.safestring import mark_safe
from django.core.exceptions import ValidationError

class RestaurantForm(forms.ModelForm):
    id = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
    )

    cuisines = forms.JSONField(
        label='Cuisines',
        widget=forms.Textarea(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
        required=True,
        help_text='Enter a valid JSON array, e.g., ["European", "Asian", "Indonesian"]'
    )
    class Meta:
        model = Restaurant
        fields = '__all__'  # Use all fields from the model
        widgets = {
            'id': forms.TextInput(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
            'name': forms.TextInput(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
            'description': forms.Textarea(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
            'reviews': forms.NumberInput(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
            'rating': forms.NumberInput(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
            'link': forms.URLInput(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
            'email': forms.EmailInput(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
            'phone': forms.TextInput(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
            'website': forms.URLInput(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
            'image_url': forms.URLInput(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
            'address': forms.TextInput(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
            'latitude': forms.NumberInput(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
            'longitude': forms.NumberInput(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
            'price_range': forms.TextInput(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
            'ranking': forms.Textarea(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
            'detailed_address': forms.Textarea(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
            'reviews_per_rating': forms.Textarea(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
            'review_keywords': forms.Textarea(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
            'open_hours': forms.Textarea(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
            'menu_link': forms.URLInput(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
            'delivery_url': forms.URLInput(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
            'cuisines': forms.TextInput(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
            'diets': forms.Textarea(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
            'meal_types': forms.Textarea(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
            'dining_options': forms.Textarea(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
            'owner_types': forms.Textarea(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
            'top_tags': forms.Textarea(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
            'is_open': forms.CheckboxInput(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
        }

    def __init__(self, *args, **kwargs):
        super(RestaurantForm, self).__init__(*args, **kwargs)
        required_fields = ['id', 'name', 'latitude', 'longitude', 'cuisines', 'website', 'phone', 'address']
        for field_name in required_fields:
            self.fields[field_name].required = True

        # Add red asterisk for required fields
        for field_name, field in self.fields.items():
            if field.required:
                if not field.label:
                    # Assign a default label if it's None
                    field.label = field_name.replace('_', ' ').capitalize()
                field.label = mark_safe(f'{field.label} <span class="text-red-500">*</span>')

    def clean_id(self):
        id = self.cleaned_data['id']
        if Restaurant.objects.filter(id=id).exists():
            if not self.instance.pk or self.instance.id != id:
                raise ValidationError('A restaurant with this ID already exists.')
        return id

from restaurants.models import Restaurant
from django import forms
from django.utils.safestring import mark_safe

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'
        widgets = {
            'osm_id': forms.TextInput(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
            'name': forms.TextInput(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
            'latitude': forms.NumberInput(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
            'longitude': forms.NumberInput(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
            'amenity': forms.TextInput(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
            'cuisine': forms.TextInput(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
            'city': forms.TextInput(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
            'street': forms.TextInput(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
            'housenumber': forms.TextInput(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
            'postcode': forms.TextInput(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
            'email': forms.EmailInput(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
            'phone': forms.TextInput(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
            'website': forms.URLInput(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
            'image_url': forms.URLInput(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
        }

    def __init__(self, *args, **kwargs):
        super(RestaurantForm, self).__init__(*args, **kwargs)
        # Make specific fields required
        self.fields['name'].required = True
        self.fields['latitude'].required = True
        self.fields['longitude'].required = True
        self.fields['amenity'].required = True
        self.fields['city'].required = True
        self.fields['cuisine'].required = True
        self.fields['street'].required = True

        # Automatically add a red asterisk for required fields in labels
        for field_name, field in self.fields.items():
            if field.required:
                field.label = mark_safe(f'{field.label} <span class="text-red-500">*</span>')

        # This will automatically show red asterisks for all required fields

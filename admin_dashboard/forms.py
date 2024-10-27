from restaurants.models import Restaurant
from django import forms
from django.utils.safestring import mark_safe
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

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
        required_fields = ['id', 'name', 'latitude', 'longitude', 'cuisines', 'phone', 'address']
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


class UserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
        required=False,
        label='Password'  # Will adjust label in __init__
    )
    password_confirm = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
        required=False,
        label='Confirm Password'  # Will adjust label in __init__
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'is_active', 'is_superuser']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
            'email': forms.EmailInput(attrs={'class': 'border border-gray-300 p-2 rounded-md w-full'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'h-4 w-4'}),
            'is_superuser': forms.CheckboxInput(attrs={'class': 'h-4 w-4'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        required_fields = ['username', 'email']
        for field_name in required_fields:
            self.fields[field_name].required = True

        if self.instance.pk:
            # Updating existing user
            self.fields['password'].label = 'New Password'
            self.fields['password'].required = False
            self.fields['password_confirm'].label = 'Confirm New Password'
            self.fields['password_confirm'].required = False
            self.fields['password'].help_text = 'Leave blank to keep the current password.'
        else:
            # Adding new user
            self.fields['password'].label = 'Password'
            self.fields['password'].required = True
            self.fields['password_confirm'].label = 'Confirm Password'
            self.fields['password_confirm'].required = True

        # Add red asterisk to required fields
        for field_name, field in self.fields.items():
            if field.required:
                if field_name == 'is_superuser':
                    field.label = 'Admin <span class="text-red-500">*</span>'
                else:
                    field.label = mark_safe(f'{field.label} <span class="text-red-500">*</span>')
            else:
                if field_name == 'is_superuser':
                    field.label = 'Admin'

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if self.instance.pk:
            # Updating existing user
            if password:
                # If password is provided, check if it matches the confirmation
                if password != password_confirm:
                    self.add_error('password_confirm', 'New passwords do not match.')
        else:
            # Adding new user
            if not password:
                self.add_error('password', 'Password is required.')
            if password != password_confirm:
                self.add_error('password_confirm', 'Passwords do not match.')

        return cleaned_data

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        password = self.cleaned_data.get('password')

        if password:
            user.set_password(password)
        elif not self.instance.pk:
            # Password is required for new users
            pass  # Should not reach here due to validation

        # Set is_staff to same as is_superuser
        user.is_staff = user.is_superuser

        if commit:
            user.save()
        return user
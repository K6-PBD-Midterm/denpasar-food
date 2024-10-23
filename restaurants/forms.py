from django import forms

class RestaurantFilterForm(forms.Form):
    search_by = forms.ChoiceField(choices=[
        ('name', 'Name'),
        ('cuisine', 'Cuisine'),
        ('city', 'City'),
        ('street', 'Street'),
        ('postcode', 'Postcode')
    ], required=False, label='Search By')
    search = forms.CharField(required=False, label='Search')
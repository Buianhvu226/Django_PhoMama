from django import forms
from .models import Food

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['FoodName', 'Category', 'Price', 'Quantity', 'ImageFood', 'Description']

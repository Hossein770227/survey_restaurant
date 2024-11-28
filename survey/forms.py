from django import forms

from .models import FoodQuality

class FoodForm(forms.ModelForm):
    class Meta:
        model = FoodQuality
        fields = ['food','choice_quality']
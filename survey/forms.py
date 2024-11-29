from django import forms

from .models import FoodQuality, Cleaning

class FoodForm(forms.ModelForm):
    class Meta:
        model = FoodQuality
        fields = ['food','choice_quality']


class CleanForm(forms.ModelForm):
    class Meta:
        model = Cleaning
        fields = ['cleaning_the_area','costomer_score']



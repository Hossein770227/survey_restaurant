from django import forms

from .models import FoodQuality, Cleaning, SurveyAboutUs

class FoodForm(forms.ModelForm):
    class Meta:
        model = FoodQuality
        fields = ['food','choice_quality']


class SurveyAboutUsForm(forms.ModelForm):
    class Meta:
        model = SurveyAboutUs
        fields = ['strength','yes_or_no']



class CleanForm(forms.ModelForm):
    class Meta:
        model = Cleaning
        fields = ['cleaning_the_area','costomer_score']




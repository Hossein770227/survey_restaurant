from django.shortcuts import render

from .models import OurStrengths
from .forms import FoodForm, CleanForm

def survey_page_view(request):
    return render(request, 'survey/survey.html')


def survey_list_view(request):
    if request.method =='POST':
        food_form = FoodForm(request.POST)
        if food_form.is_valid():
            food_form.save()
            food_form = FoodForm()
    else:
        food_form = FoodForm()
    return render(request, 'survey/survey_list.html', context={'form':food_form})


def our_strengths_view(request):
    queryset_strengths = OurStrengths.objects.all()
    
    return render(request, 'survey/survey_list.html', context={'strengths':queryset_strengths})



def survey_clean_view(request):
    if request.method =='POST':
        clean_form = CleanForm(request.POST)
        if clean_form.is_valid():
            clean_form.save()
            clean_form = CleanForm()          
    else:
        clean_form = CleanForm()
     
    return render(request, 'survey/survey_clean.html', context={'survey_clean':clean_form})

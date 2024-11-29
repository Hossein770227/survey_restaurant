from django.shortcuts import render

from .models import OurStrengths
from .forms import FoodForm

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
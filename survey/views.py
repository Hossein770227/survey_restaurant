from django.shortcuts import render

from .models import FoodQuality
from .forms import FoodForm

def survey_page_view(request):
    return render(request, 'survey/survey.html')


def survey_list_view(request):
    queryset = FoodQuality.objects.filter(is_active = True)
    return render(request, 'survey/survey_list.html', context={'foods':queryset, 'form':FoodForm()})


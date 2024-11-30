from django.urls import path

from . import views

app_name = 'survey'


urlpatterns = [
    path('', views.survey_page_view, name='survey'),
    path('food/', views.survey_list_view, name='survey_food'),
    path('about/', views.survey_abuout_us_view, name='about'),
    path('clean/', views.survey_clean_view, name='clean'),
]

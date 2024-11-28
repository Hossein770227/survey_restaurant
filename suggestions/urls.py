from django.urls import path

from . import views

app_name = 'suggestions'

urlpatterns = [
    path('', views.suggestions_from_customer, name='suggestions'),
]

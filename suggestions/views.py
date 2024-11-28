from django.shortcuts import render

def suggestions_from_customer(request):
    return render(request, 'suggestions/customer_suggestions.html')

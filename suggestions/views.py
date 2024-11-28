from django.shortcuts import render

from .forms import CommentSuggestionsForm

def suggestions_from_customer(request):
    if request.method =='POST':
        form = CommentSuggestionsForm(request.POST)
        if form.is_valid():
            form.save()
            form = CommentSuggestionsForm()
    else:
        form = CommentSuggestionsForm()
    return render(request, 'suggestions/customer_suggestions.html', {'form':form})

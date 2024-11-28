from django.contrib import admin

from .models import CommentsSuggestions


@admin.register(CommentsSuggestions)
class CommentsSuggestionsAdmin(admin.ModelAdmin):
    list_display=['date_time_created']

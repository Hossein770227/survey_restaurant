from django.contrib import admin

from .models import  Food, FoodQuality



@admin.register(Food)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','is_active',]
    search_fields = ['title']



@admin.register(FoodQuality)
class FoodQualityAdmin(admin.ModelAdmin):
    list_display = ['food','choice_quality','is_active',]
    search_fields = ['title']
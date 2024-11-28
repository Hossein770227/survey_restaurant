from django.contrib import admin

from .models import  Food, FoodQuality, OurStrengths, SurveyAboutUs


class FoodQualityInLine(admin.TabularInline):
    model = FoodQuality
    fields = ['choice_quality','is_active',]
    extra = 0


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['title','is_active',]
    search_fields = ['title']
    inlines = [FoodQualityInLine]
    



# @admin.register(FoodQuality)
# class FoodQualityAdmin(admin.ModelAdmin):
#     list_display = ['food','choice_quality','is_active',]
#     search_fields = ['title']


@admin.register(OurStrengths)
class OurStrengthAdmin(admin.ModelAdmin):
    list_display = ['Strength','is_active','date_time_created',]
    search_fields = ['Strength',]



@admin.register(SurveyAboutUs)
class SurveyAboutUs(admin.ModelAdmin):
    list_display = ['strength','yes_or_no','date_time_created',]
    search_fields = ['Strength',]
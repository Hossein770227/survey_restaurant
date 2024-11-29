from django.contrib import admin

from .models import  Cleaning, CollectionCleaning, Food, FoodQuality, OurStrengths, SurveyAboutUs


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

class SurveyAboutUsInLine(admin.TabularInline):
    model = SurveyAboutUs
    fields = ['yes_or_no',]
    extra = 1


@admin.register(OurStrengths)
class OurStrengthAdmin(admin.ModelAdmin):
    list_display = ['title','is_active','date_time_created',]
    search_fields = ['title',]
    inlines = [SurveyAboutUsInLine]



# @admin.register(SurveyAboutUs)
# class SurveyAboutUs(admin.ModelAdmin):
#     list_display = ['strength','yes_or_no','date_time_created',]
#     search_fields = ['Strength',]





class CleaningSocoreCustomerInLine(admin.TabularInline):
    model = Cleaning
    fields = ['costomer_score',]
    extra = 0


@admin.register(CollectionCleaning)
class CollectionCleaningAdmin(admin.ModelAdmin):
    list_display = ['title','is_active','date_time_created',]
    inlines =[CleaningSocoreCustomerInLine]


# @admin.register(Cleaning)
# class CleaningScoreCustomer(admin.ModelAdmin):
#     list_display = ['cleaning_the_area','costomer_score','date_time_created',]
from django.db import models
from django.utils.translation import gettext as _ 


class Food(models.Model):
    title = models.CharField(_("title"), max_length=255)
    is_active = models.BooleanField(_("active"), default=True)
    date_time_created = models.DateField(_("date created"),  auto_now_add=True)

    class Meta:
        verbose_name =_("food")
        verbose_name_plural = _("food")

    def __str__(self):
        return self.title


class FoodQuality(models.Model):
    CHOICES = (
        ('4', _('perfect')),
        ('3', _('good')),
        ('2', _('manual')),
        ('1', _('bad')),
    )
    food = models.ForeignKey(Food, verbose_name=_("food"), on_delete=models.CASCADE)
    choice_quality = models.CharField(_('quality'), choices =CHOICES, max_length = 50)
    is_active = models.BooleanField(_("active"), default=True)

    class Meta:
        verbose_name =_("food quality")
        verbose_name_plural = _("food quality")


    def __str__(self):
        return self.food.title
    


class OurStrengths(models.Model):
    title = models.CharField(_("strength"), max_length=255)
    is_active = models.BooleanField(_("active"), default=True)
    date_time_created = models.DateTimeField(_("date time created"),  auto_now_add=True)

    class Meta:
        verbose_name =_("Strength")
        verbose_name_plural = _("Strength")


    def __str__(self):
        return self.title



class SurveyAboutUs(models.Model):
    strength = models.ForeignKey(OurStrengths, verbose_name=_("strength"), on_delete=models.CASCADE)
    yes_or_no = models.BooleanField(_("yes or no"), default=False)
    date_time_created = models.DateTimeField(_("date time created"),  auto_now_add=True)

    class Meta:
        verbose_name =_("survey about us")
        verbose_name_plural = _("survey about us")

    

#  Collection cleaning moldels

class CollectionCleaning(models.Model):
    title = models.CharField(_("title"), max_length=255)
    is_active = models.BooleanField(_("active"), default=True)
    date_time_created = models.DateField(_("date created"),  auto_now_add=True)

    class Meta:
        verbose_name =_("collection")
        verbose_name_plural = _("collection")

    def __str__(self):
        return self.title


class Cleaning(models.Model):
    CHOICES = (
        ('4', _('perfect')),
        ('3', _('good')),
        ('2', _('manual')),
        ('1', _('bad')),
    )
    cleaning_the_area = models.ForeignKey(CollectionCleaning, verbose_name=_("cleannig area"), on_delete=models.CASCADE)
    costomer_score = models.CharField(_("customer score"),choices=CHOICES, max_length=50)
    date_time_created = models.DateField(_("date created"),  auto_now_add=True)

    class Meta:
        verbose_name =_("coustomer score for cleaning ")
        verbose_name_plural = _("coustomer score for cleaning ")


    def __str__(self):
        return self.costomer_score


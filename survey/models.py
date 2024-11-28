from django.db import models
from django.utils.translation import gettext as _ 


class Food(models.Model):
    title = models.CharField(_("title"), max_length=255)
    is_active = models.BooleanField(_("active"), default=True)
    date_time_created = models.DateField(_("date created"),  auto_now_add=True)

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


    def __str__(self):
        return self.title
    
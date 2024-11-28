from django.db import models
from django.utils.translation import gettext as _ 



class CommentsSuggestions(models.Model):
    text = models.TextField(_("text"))
    date_time_created = models.DateTimeField(_("date time created"), auto_now_add=True)

   
    class Meta:
        verbose_name =_("comments and suggestions ")
        verbose_name_plural = _("comments and suggestions ")

    
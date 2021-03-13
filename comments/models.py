from articles.models import ArticleModel,UserInformation
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.


class CommentModel(models.Model):

    body = models.TextField(_("body"), max_length=255)
    user = models.ForeignKey(
        UserInformation, verbose_name=_("user"), on_delete=models.CASCADE)
    article = models.ForeignKey(
        ArticleModel, verbose_name=_("article"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("commentmodel")
        verbose_name_plural = _("commentmodels")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("commentmodel_detail", kwargs={"pk": self.pk})

from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from users.models import UserInformation
from django.utils.translation import gettext_lazy as _
# Create your models here.


class ArticleModel(models.Model):

    title = models.CharField("title", max_length=50)
    author = models.ForeignKey(
        UserInformation, verbose_name="user", on_delete=models.CASCADE)
    body = models.FileField("file", upload_to="articels/", max_length=100)

    tags = TaggableManager()

    class Meta:
        verbose_name = "articlemodel"
        verbose_name_plural = "articlemodels"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("articlemodel_detail", kwargs={"pk": self.pk})

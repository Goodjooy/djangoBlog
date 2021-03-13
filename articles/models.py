from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from users.models import UserInformation
from django.utils.translation import gettext_lazy as _
from  django.utils import timezone
# Create your models here.


class ArticleModel(models.Model):

    title = models.CharField("title", max_length=50)
    author = models.ForeignKey(
        UserInformation, verbose_name="user", on_delete=models.CASCADE)
    body = models.FileField("file", upload_to="articles/markdown", max_length=100)

    createTime=models.DateTimeField(_("create time"), auto_now=False, auto_now_add=True)
    modifyTime=models.DateTimeField(_("modify time"), auto_now=True, auto_now_add=False)

    tags = TaggableManager()

    class Meta:
        verbose_name = "articlemodel"
        verbose_name_plural = "articlemodels"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("articlemodel_detail", kwargs={"pk": self.pk})

class ArticleImage(models.Model):

    image = models.ImageField(_("image"), upload_to="articles/image", height_field=None, width_field=None, max_length=100)
    article=models.ForeignKey(ArticleModel, verbose_name=_(""), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("articleimage")
        verbose_name_plural = _("articleimages")

    def __str__(self):
        return self.image.__str__()

    def get_absolute_url(self):
        return reverse("articleimage_detail", kwargs={"pk": self.pk})

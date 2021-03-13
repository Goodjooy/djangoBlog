from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.


class UserInformation(models.Model):

    user = models.OneToOneField(
        User, verbose_name="user", on_delete=models.CASCADE)

    headImage = models.ImageField("head", upload_to="user/head")

    discript = models.TextField("discript", max_length=255)

    class Meta:
        verbose_name = "userinformation"
        verbose_name_plural = "userinformations"

    def __str__(self):
        return self.user.__str__()

    def get_absolute_url(self):
        return reverse("userinformation_detail", kwargs={"pk": self.pk})

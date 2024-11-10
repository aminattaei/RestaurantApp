from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(_("عنوان"), max_length=50)
    description = models.TextField(_("توضیح"))
    content = models.TextField(_("متن"))
    created_time = models.DateTimeField(_("زمان انتشار"), default=timezone.now)
    author = models.ForeignKey(
        User, verbose_name=_("نویسنده"), on_delete=models.CASCADE
    )
    image = models.ImageField(_("تصویر"), upload_to="blogs/", blank=True, null=True)
    category = models.ForeignKey(
        "Category",
        verbose_name=_("دسته بندی"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(_("عنوان"), max_length=50)
    slug = models.SlugField(_("عنوان لاتین"))
    published_at = models.DateTimeField(_("زمان انتشار"), auto_now_add=True)

    def __str__(self):
        return self.title

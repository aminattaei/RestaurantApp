from django.db import models
from django.utils.translation import gettext as _


# SELF CODE


class Food(models.Model):
    FOOD_TYPE = [
        ("breakfast", "صبحانه"),
        ("lunch", "ناهار"),
        ("dinner", "شام"),
        ("drinks", "نوشیدنی"),
        # ("Dessert", "دسر"),
        # ("Appetizer", "پیش غذا"),
    ]
    name = models.CharField(_("نام غذا"), max_length=50)
    description = models.TextField(_("توضیحات"))
    rate = models.IntegerField(_("امتیاز"), default=0)
    price = models.IntegerField(_("قیمت"), default=0)
    time = models.IntegerField(_("زمان لازم"), default=0)
    type_food = models.CharField(
        _("نوع غذا"), max_length=10, choices=FOOD_TYPE, default="lunch"
    )
    published_date = models.DateField(_("تاریخ انتشار"), auto_now_add=True)
    photo = models.ImageField(_("تصویر محصول"), upload_to="foods/")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "foods"
        verbose_name = "food"
        verbose_name_plural = "foods"


# ----------------------------------------------------------
# AI CODE

# class FoodType(models.Model):
#     name = models.CharField(_("نام نوع غذا"), max_length=50)

#     def __str__(self):
#         return self.name

# class Food(models.Model):
#     name = models.CharField(_("نام غذا"), max_length=50)
#     description = models.TextField(_("توضیحات"))
#     rate = models.IntegerField(_("امتیاز"), default=0)
#     price = models.IntegerField(_('قیمت'), default=0)
#     time=models.IntegerField(_('زمان لازم'),default=0)
#     published_date=models.DateField(_("تاریخ انتشار"),auto_now_add=True)
#     photo=models.ImageField(_("تصویر محصول"), upload_to='foods/',height_field=None, width_field=None)

#     types = models.ManyToManyField(FoodType, verbose_name=_("نوع غذا"))

#     def __str__(self):
#         return self.name

#     class Meta:
#         db_table = 'foods'
#         verbose_name = 'food'
#         verbose_name_plural = 'foods'

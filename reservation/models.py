from django.db import models
from django.utils.translation import gettext as _
from datetime import *


class reservation(models.Model):
    name = models.CharField(_("نام و نام خانوادگی"), max_length=50)
    email = models.EmailField(_("ایمیل"), max_length=254)
    phoneNumber = models.CharField(_("شماره تماس"), max_length=20)
    ReservationDay = models.DateField(_("روز رزرو"))
    ReservationTime = models.TimeField(_("ساعت رزرو"))
    CountOfPerson = models.IntegerField(_("تعداد افراد"), default=2)

    class Meta:
        db_table = "reservation"
        verbose_name = "reservation"
        verbose_name_plural = "reservations"

    def __str__(self):
        return self.name

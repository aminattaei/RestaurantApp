from django.contrib import admin
from .models import reservation




@admin.register(reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display=['name','email','ReservationDay','ReservationTime','CountOfPerson']
    search_fields=['name','ReservationDay','ReservationTime']

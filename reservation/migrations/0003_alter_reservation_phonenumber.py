# Generated by Django 5.1.2 on 2024-11-06 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_reservation_countofperson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='phoneNumber',
            field=models.CharField(max_length=20, verbose_name='شماره تماس'),
        ),
    ]

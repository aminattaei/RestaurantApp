# Generated by Django 5.1.2 on 2024-11-03 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0008_alter_food_type_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='type_food',
            field=models.CharField(choices=[('breakfast', 'صبحانه'), ('lunch', 'ناهار'), ('dinner', 'شام'), ('drinks', 'نوشیدنی')], default='Lunch', max_length=10, verbose_name='نوع غذا'),
        ),
    ]

# Generated by Django 5.1.2 on 2024-11-02 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0007_remove_food_types_food_type_food_delete_foodtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='type_food',
            field=models.CharField(choices=[('Lunch', 'ناهار'), ('Dinner', 'شام'), ('Drinks', 'نوشیدنی')], default='Lunch', max_length=10, verbose_name='نوع غذا'),
        ),
    ]

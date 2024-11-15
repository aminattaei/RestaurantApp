# Generated by Django 5.1.2 on 2024-11-02 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0006_foodtype_remove_food_type_food_food_types'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='types',
        ),
        migrations.AddField(
            model_name='food',
            name='type_food',
            field=models.CharField(choices=[('Breakfast', 'صبحانه'), ('Lunch', 'ناهار'), ('Dinner', 'شام'), ('Drink', 'نوشیدنی'), ('Dessert', 'دسر'), ('Appetizer', 'پیش غذا')], default='Lunch', max_length=10, verbose_name='نوع غذا'),
        ),
        migrations.DeleteModel(
            name='FoodType',
        ),
    ]

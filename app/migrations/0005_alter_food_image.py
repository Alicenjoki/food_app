# Generated by Django 4.2.5 on 2023-09-21 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_food_price_alter_course_name_alter_food_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.ImageField(default='food_default.webp', upload_to='food_pics/'),
        ),
    ]
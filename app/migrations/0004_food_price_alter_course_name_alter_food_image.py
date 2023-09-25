# Generated by Django 4.2.5 on 2023-09-21 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_food_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='price',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(choices=[('none', 'none'), ('starter', 'starter'), ('main_course', 'main_course'), ('dessert', 'dessert'), ('Gin', 'Gin'), ('Whisky', 'Whisky'), ('Vodka', 'Vodka')], max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.ImageField(default='food_default.webp', null=True, upload_to='food_pics'),
        ),
    ]

# Generated by Django 4.2.5 on 2023-09-22 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_cart_options_alter_cartitem_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name_plural': 'cart'},
        ),
        migrations.AlterModelOptions(
            name='cartitem',
            options={'verbose_name_plural': 'Cartitem'},
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name_plural': 'course'},
        ),
        migrations.AlterModelOptions(
            name='food',
            options={'ordering': ('-created',), 'verbose_name_plural': 'food'},
        ),
        migrations.AlterModelOptions(
            name='meal',
            options={'verbose_name_plural': 'meal'},
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='app.food'),
        ),
    ]

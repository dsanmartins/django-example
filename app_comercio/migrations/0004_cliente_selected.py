# Generated by Django 4.1.7 on 2023-06-23 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_comercio', '0003_computador_imagen_producto_monitor_imagen_producto_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='selected',
            field=models.BooleanField(default=False),
        ),
    ]
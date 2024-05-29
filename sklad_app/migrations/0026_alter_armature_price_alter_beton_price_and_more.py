# Generated by Django 4.0.6 on 2024-04-03 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklad_app', '0025_lists_lopasti_tube_wirehousev'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armature',
            name='price',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='beton',
            name='price',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='wire',
            name='price',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='wire4',
            name='price',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='wire6',
            name='price',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=10),
        ),
    ]

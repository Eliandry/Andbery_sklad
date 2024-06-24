# Generated by Django 4.0.6 on 2024-06-17 14:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sklad_app', '0055_operationdeparture_extra_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='senddetail',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='operationdeparture',
            name='extra_details',
            field=models.TextField(blank=True, default=' ', null=True),
        ),
    ]

# Generated by Django 4.0.6 on 2024-03-26 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklad_app', '0022_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operationarrival',
            name='pile',
        ),
        migrations.RemoveField(
            model_name='operationarrival',
            name='quantity',
        ),
        migrations.AddField(
            model_name='operationarrival',
            name='details',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.0.6 on 2024-04-16 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sklad_app', '0035_operationarrival_v'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operationarrival_v',
            name='price_part',
        ),
    ]
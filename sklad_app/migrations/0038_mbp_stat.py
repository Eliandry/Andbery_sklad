# Generated by Django 4.0.6 on 2024-04-18 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklad_app', '0037_order_v'),
    ]

    operations = [
        migrations.CreateModel(
            name='MBP_stat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('details', models.TextField()),
                ('brigade', models.CharField(max_length=200)),
            ],
        ),
    ]

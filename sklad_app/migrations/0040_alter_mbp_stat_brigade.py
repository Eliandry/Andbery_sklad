# Generated by Django 4.0.6 on 2024-04-18 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklad_app', '0039_mbp_stat_admission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mbp_stat',
            name='brigade',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
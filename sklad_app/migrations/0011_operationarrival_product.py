# Generated by Django 4.2.5 on 2024-03-07 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sklad_app', '0010_operationproduction'),
    ]

    operations = [
        migrations.AddField(
            model_name='operationarrival',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sklad_app.operationproduction'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.5 on 2024-03-06 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklad_app', '0008_alter_car_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(choices=[('Маз', 'Маз'), ('Камаз', 'Камаз'), ('Хино', 'Хино'), ('FAW', 'FAW'), ('Мерседес', 'Мерседес')], max_length=30),
        ),
    ]

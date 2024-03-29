# Generated by Django 4.2.6 on 2024-03-04 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sklad_app', '0006_rename_confirm_operationarrival_confirm_b'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=123)),
                ('number', models.CharField(max_length=123)),
                ('weight', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='operationdeparture',
            name='number_car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sklad_app.car'),
        ),
    ]

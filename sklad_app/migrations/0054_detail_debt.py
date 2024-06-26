# Generated by Django 4.0.6 on 2024-06-13 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sklad_app', '0053_remove_sendoperation_confirm_senddetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail_Debt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField()),
                ('confirm', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('brigade', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='sklad_app.brigadework')),
            ],
        ),
    ]

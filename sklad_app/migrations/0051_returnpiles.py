# Generated by Django 4.0.6 on 2024-05-15 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sklad_app', '0050_userbrigade'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReturnPiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('details', models.TextField()),
                ('description', models.CharField(blank=True, max_length=500)),
                ('confirm_s', models.BooleanField(default=False)),
                ('confirm_sklad', models.BooleanField(default=False)),
                ('brigade', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='sklad_app.brigadework')),
            ],
        ),
    ]

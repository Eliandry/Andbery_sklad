# Generated by Django 4.2.5 on 2024-03-07 08:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sklad_app', '0009_alter_car_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='OperationProduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('confirm_b', models.BooleanField(default=False)),
                ('pile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sklad_app.pile')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

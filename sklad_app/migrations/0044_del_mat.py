# Generated by Django 4.0.6 on 2024-04-25 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklad_app', '0043_order_total_armature10'),
    ]

    operations = [
        migrations.CreateModel(
            name='Del_mat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_beton', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('total_wire_3', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('total_wire_4', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('total_wire_6', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('total_armature', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('total_armature10', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

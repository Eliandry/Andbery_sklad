# Generated by Django 4.2.5 on 2024-03-22 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklad_app', '0019_wire4_wire6_operationdeparture_confirm_bb'),
    ]

    operations = [
        migrations.CreateModel(
            name='WirehouseB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('armature', models.IntegerField(default=0)),
                ('wire3', models.IntegerField(default=0)),
                ('wire4', models.IntegerField(default=0)),
                ('wire6', models.IntegerField(default=0)),
            ],
        ),
    ]

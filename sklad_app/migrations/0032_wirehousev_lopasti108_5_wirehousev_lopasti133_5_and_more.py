# Generated by Django 4.0.6 on 2024-04-16 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklad_app', '0031_lists5'),
    ]

    operations = [
        migrations.AddField(
            model_name='wirehousev',
            name='lopasti108_5',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='wirehousev',
            name='lopasti133_5',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='wirehousev',
            name='lopasti89_5',
            field=models.IntegerField(default=0),
        ),
    ]

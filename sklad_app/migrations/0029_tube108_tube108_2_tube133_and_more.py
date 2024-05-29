# Generated by Django 4.0.6 on 2024-04-12 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklad_app', '0028_mbp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tube108',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('company_sell', models.CharField(max_length=200)),
                ('company_buy', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tube108_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('company_sell', models.CharField(max_length=200)),
                ('company_buy', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tube133',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('company_sell', models.CharField(max_length=200)),
                ('company_buy', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='wirehousev',
            old_name='lists',
            new_name='lists4',
        ),
        migrations.RenameField(
            model_name='wirehousev',
            old_name='tube',
            new_name='lists5',
        ),
        migrations.AddField(
            model_name='wirehousev',
            name='tube108',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='wirehousev',
            name='tube108_2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='wirehousev',
            name='tube133',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='wirehousev',
            name='tube89',
            field=models.IntegerField(default=0),
        ),
    ]

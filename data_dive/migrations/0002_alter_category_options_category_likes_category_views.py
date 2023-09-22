# Generated by Django 4.0.2 on 2023-09-09 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_dive', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='category',
            name='views',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
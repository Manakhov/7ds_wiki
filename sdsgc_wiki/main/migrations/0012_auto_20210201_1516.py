# Generated by Django 3.1.5 on 2021-02-01 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_properties'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='heroes',
            name='properties',
        ),
        migrations.AddField(
            model_name='heroes',
            name='properties',
            field=models.ManyToManyField(to='main.Properties', verbose_name='Свойства'),
        ),
    ]

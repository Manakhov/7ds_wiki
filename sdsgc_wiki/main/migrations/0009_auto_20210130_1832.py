# Generated by Django 3.1.5 on 2021-01-30 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210130_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heroes',
            name='ignition',
            field=models.BooleanField(null=True, verbose_name='Воспламенение'),
        ),
        migrations.AlterField(
            model_name='heroes',
            name='weakness',
            field=models.BooleanField(null=True, verbose_name='Слабое место'),
        ),
    ]

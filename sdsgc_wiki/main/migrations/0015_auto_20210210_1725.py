# Generated by Django 3.1.5 on 2021-02-10 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20210210_1722'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='properties',
            options={'ordering': ['name'], 'verbose_name': 'Свойство', 'verbose_name_plural': 'Свойства'},
        ),
        migrations.AlterOrderWithRespectTo(
            name='properties',
            order_with_respect_to=None,
        ),
    ]

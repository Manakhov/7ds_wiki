# Generated by Django 3.1.5 on 2021-02-10 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20210202_1726'),
    ]

    operations = [
        migrations.AlterOrderWithRespectTo(
            name='properties',
            order_with_respect_to='name',
        ),
    ]

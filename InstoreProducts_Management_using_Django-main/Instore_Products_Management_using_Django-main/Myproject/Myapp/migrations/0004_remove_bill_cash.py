# Generated by Django 4.1.4 on 2023-01-27 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0003_bill_cash'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='cash',
        ),
    ]

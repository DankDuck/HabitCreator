# Generated by Django 5.0.7 on 2024-08-16 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0007_alter_basichabit_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basichabit',
            name='owner',
        ),
    ]

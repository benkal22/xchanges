# Generated by Django 5.0.6 on 2024-06-21 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
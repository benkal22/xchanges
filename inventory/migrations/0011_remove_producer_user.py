# Generated by Django 5.0.6 on 2024-06-22 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_alter_producer_user_remove_producer_groups_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producer',
            name='user',
        ),
    ]

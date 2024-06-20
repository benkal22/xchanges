# Generated by Django 5.0.6 on 2024-06-20 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_alter_producer_options_alter_producer_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producer',
            name='is_approved',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='producer',
            name='is_active',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]

# Generated by Django 5.1.4 on 2025-01-19 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Settings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='address',
            field=models.TextField(default='', max_length=200),
            preserve_default=False,
        ),
    ]

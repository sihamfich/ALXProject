# Generated by Django 5.1.4 on 2025-01-06 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Property', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='Slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]

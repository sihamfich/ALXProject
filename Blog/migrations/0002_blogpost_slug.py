# Generated by Django 5.1.4 on 2025-01-06 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='Slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]

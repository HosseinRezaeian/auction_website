# Generated by Django 5.0.4 on 2024-04-19 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productorservice',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]

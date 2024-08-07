# Generated by Django 5.0.6 on 2024-07-06 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_picture_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='productorservice',
            name='first_pic',
            field=models.ImageField(blank=True, null=True, upload_to='pictures'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(upload_to='pictures'),
        ),
    ]

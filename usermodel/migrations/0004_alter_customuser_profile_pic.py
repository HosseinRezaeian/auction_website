# Generated by Django 5.0.6 on 2024-07-05 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermodel', '0003_alter_customuser_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='media/pictures/'),
        ),
    ]

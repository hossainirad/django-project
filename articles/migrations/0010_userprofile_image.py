# Generated by Django 2.0.3 on 2018-04-13 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_auto_20180410_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]

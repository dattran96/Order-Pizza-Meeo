# Generated by Django 3.1.4 on 2021-01-03 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='picture',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='pictures/'),
        ),
    ]

# Generated by Django 3.1.4 on 2021-01-04 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='title',
            field=models.CharField(default='no title', max_length=150),
            preserve_default=False,
        ),
    ]

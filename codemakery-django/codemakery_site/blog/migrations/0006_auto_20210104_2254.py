# Generated by Django 3.1.4 on 2021-01-04 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='title',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post'),
            preserve_default=False,
        ),
    ]

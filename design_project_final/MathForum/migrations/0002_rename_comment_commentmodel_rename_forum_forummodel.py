# Generated by Django 4.1.5 on 2023-02-26 21:13

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MathForum', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='CommentModel',
        ),
        migrations.RenameModel(
            old_name='Forum',
            new_name='ForumModel',
        ),
    ]

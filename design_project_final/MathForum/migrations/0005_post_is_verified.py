# Generated by Django 4.1.5 on 2023-04-09 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MathForum', '0004_alter_post_description_alter_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]

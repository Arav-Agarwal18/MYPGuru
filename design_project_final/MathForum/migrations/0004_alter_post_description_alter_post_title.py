# Generated by Django 4.1.5 on 2023-03-09 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MathForum', '0003_category_comment_post_remove_forummodel_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]

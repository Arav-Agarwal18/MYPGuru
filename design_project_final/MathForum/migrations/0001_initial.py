# Generated by Django 4.1.5 on 2023-02-26 19:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to='')),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('Task Specific Clarifications', 'Task Specific Clarifications'), ('Task Sheets', 'Task Sheets'), ('Notes', 'Notes'), ('Sample Answers', 'Sample Answers'), ('Sample Papers', 'Sample Papers')], max_length=28)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MathForum.forum')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

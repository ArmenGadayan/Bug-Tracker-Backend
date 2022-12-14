# Generated by Django 4.0.6 on 2022-07-18 00:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0014_remove_project_members_member'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='project',
        ),
        migrations.AddField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(blank=True, null=True, related_name='projects', to=settings.AUTH_USER_MODEL),
        ),
    ]

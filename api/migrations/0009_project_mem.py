# Generated by Django 4.0.6 on 2022-07-16 02:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0008_dev_delete_devloper'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='mem',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dev', to=settings.AUTH_USER_MODEL),
        ),
    ]

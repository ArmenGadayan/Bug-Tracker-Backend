# Generated by Django 4.0.6 on 2022-07-16 02:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0007_devloper'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dev',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='members', to='api.project')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='developer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Devloper',
        ),
    ]

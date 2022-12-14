# Generated by Django 4.0.6 on 2022-07-20 20:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0024_alter_bug_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='status',
            field=models.CharField(choices=[('N', 'New'), ('I', 'In Progress'), ('R', 'Resolved'), ('A', 'Additional Info Required')], default='N', max_length=1),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='member', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(blank=True, null=True, related_name='projects', to='api.member'),
        ),
    ]

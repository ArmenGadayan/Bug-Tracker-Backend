# Generated by Django 4.0.6 on 2022-07-20 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_alter_bug_status_member_alter_project_members'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bug',
            name='user',
        ),
        migrations.AddField(
            model_name='bug',
            name='member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bugs', to='api.member'),
        ),
    ]

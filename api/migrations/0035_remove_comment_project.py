# Generated by Django 4.0.6 on 2022-07-25 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0034_comment_bug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='project',
        ),
    ]

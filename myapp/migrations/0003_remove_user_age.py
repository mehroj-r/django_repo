# Generated by Django 5.1.6 on 2025-02-06 03:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_user_delete_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
    ]

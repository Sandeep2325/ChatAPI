# Generated by Django 5.0.3 on 2024-03-10 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]

# Generated by Django 5.0.3 on 2024-03-16 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_imagemodel_created_at_imagemodel_updated_at_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BeneiftsModel',
            new_name='BenefitsModel',
        ),
    ]
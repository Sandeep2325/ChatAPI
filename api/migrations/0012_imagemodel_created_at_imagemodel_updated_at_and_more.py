# Generated by Django 5.0.3 on 2024-03-16 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_beneiftsmodel_imagemodel_coursesmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagemodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='imagemodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='ImageBucket'),
        ),
    ]
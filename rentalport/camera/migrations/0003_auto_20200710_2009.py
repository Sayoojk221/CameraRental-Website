# Generated by Django 3.0.8 on 2020-07-10 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camera', '0002_photographerboooking_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='status',
            new_name='cameramanname',
        ),
    ]

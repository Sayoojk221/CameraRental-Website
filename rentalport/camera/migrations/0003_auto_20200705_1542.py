# Generated by Django 3.0.8 on 2020-07-05 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camera', '0002_auto_20200705_1530'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userregister',
            old_name='place',
            new_name='city',
        ),
        migrations.AddField(
            model_name='userregister',
            name='state',
            field=models.CharField(default='', max_length=200),
        ),
    ]

# Generated by Django 2.2.7 on 2019-11-19 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0019_auto_20191119_0803'),
    ]

    operations = [
        migrations.RenameField(
            model_name='day',
            old_name='day',
            new_name='day_name',
        ),
    ]

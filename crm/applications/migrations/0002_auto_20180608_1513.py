# Generated by Django 2.0.6 on 2018-06-08 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Agreement',
            new_name='Application',
        ),
    ]

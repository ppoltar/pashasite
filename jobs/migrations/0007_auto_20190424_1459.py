# Generated by Django 2.2 on 2019-04-24 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_education'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='description1',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='education',
            name='description2',
        ),
    ]

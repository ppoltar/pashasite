# Generated by Django 2.2 on 2019-04-14 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='summary',
            new_name='title',
        ),
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.CharField(default=0, max_length=400),
            preserve_default=False,
        ),
    ]
# Generated by Django 2.2 on 2019-04-24 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20190424_1009'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=100)),
                ('description1', models.CharField(max_length=5000)),
                ('description2', models.CharField(max_length=5000)),
            ],
        ),
    ]
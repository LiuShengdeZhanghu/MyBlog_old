# Generated by Django 2.0.4 on 2019-01-05 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('robot', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-create_time']},
        ),
    ]
# Generated by Django 2.0.4 on 2019-05-11 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20190511_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='comment',
        ),
        migrations.DeleteModel(
            name='Reply',
        ),
    ]

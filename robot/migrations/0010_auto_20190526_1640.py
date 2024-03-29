# Generated by Django 2.0.4 on 2019-05-26 16:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('robot', '0009_auto_20190309_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='article',
            name='blog_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='robot.BlogType'),
        ),
    ]

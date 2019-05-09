# Generated by Django 2.0.4 on 2019-03-09 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('robot', '0007_remove_article_read_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadNum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read_num', models.IntegerField(default=0, verbose_name='阅读数量')),
            ],
        ),
        migrations.RemoveField(
            model_name='article',
            name='read_num',
        ),
        migrations.AddField(
            model_name='readnum',
            name='blog',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='robot.Article'),
        ),
    ]

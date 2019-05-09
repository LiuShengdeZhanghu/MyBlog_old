# Generated by Django 2.0.4 on 2018-12-29 13:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_updated_time', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('read_num', models.IntegerField(default=0)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BlogType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='blog_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='robot.BlogType'),
        ),
    ]

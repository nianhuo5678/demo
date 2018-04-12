# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.TextField(max_length=30, null=True, blank=True)),
                ('content', models.TextField(max_length=1000, null=True, blank=True)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_liked', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('username', models.TextField(max_length=30, null=True, blank=True)),
                ('password', models.TextField(max_length=80, null=True, blank=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('info', models.TextField(null=True)),
                ('last_modified', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(related_name='user_articles', verbose_name=b'user_articles', to='blog.User', null=True),
        ),
    ]

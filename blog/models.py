# -*- encoding: utf-8 -*-
from django.db import models
from django.utils import timezone


# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True, blank=True)
    username = models.TextField(max_length=30, blank=True, null=True)
    password = models.TextField(max_length=80, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    info = models.TextField(null=True)
    last_modified = models.DateTimeField(default = timezone.now)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.username


class Article(models.Model):
    id = models.AutoField(primary_key=True, blank=False)
    title = models.TextField(max_length=30, blank=True, null=True)
    content = models.TextField(max_length=1000, blank=True, null=True)
    user = models.ForeignKey(User, verbose_name='user_articles', related_name='user_articles', null=True)
    created_time = models.DateTimeField(default = timezone.now)
    is_liked = models.BooleanField(default=False)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.title

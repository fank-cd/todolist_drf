# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Todo(models.Model):
    owner = models.ForeignKey('auth.User', related_name="Todo", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name="名字")
    done = models.BooleanField(default=False, verbose_name="是否完成")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        ordering = ('date_created',)
        verbose_name = "Todo"
        verbose_name_plural = "Todos"

    def __unicode__(self):
        return self.name

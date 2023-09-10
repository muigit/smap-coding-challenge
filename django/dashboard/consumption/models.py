# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
  id = models.IntegerField(primary_key=True)
  area = models.CharField(max_length=2)
  tariff = models.CharField(max_length=2)

class Consumption(models.Model):
  datetime = models.DateTimeField()
  consumption = models.FloatField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)

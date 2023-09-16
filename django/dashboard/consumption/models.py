# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
  id = models.IntegerField(primary_key=True)
  area = models.CharField(max_length=2)
  tariff = models.CharField(max_length=2)

class Consumption(models.Model):
  datetime = models.DateTimeField()
  consumption = models.FloatField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)

# ユーザーごとの日別集計
class AggregateUserDailyConsumption(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  date = models.DateField()
  total_consumption = models.FloatField()
  average_consumption = models.FloatField()

  class Meta:
      # 特定の組み合わせが重複しない制約
      unique_together = ('user', 'date')

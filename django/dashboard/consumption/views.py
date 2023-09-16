# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.db.models import Sum, Avg
from .models import AggregateUserDailyConsumption
from django.utils import timezone

# Create your views here.


def summary(request):
    # 全ユーザーの日付別の合計と平均消費データを取得
    date_wise_consumption_data = AggregateUserDailyConsumption.objects.values('date').annotate(
        total_consumption=Sum('total_consumption'),
        average_consumption=Avg('average_consumption')
    )

    # テンプレートコンテキストにデータを渡す
    context = {
        'date_wise_consumption_data': date_wise_consumption_data,
    }

    return render(request, 'consumption/summary.html', context)


def detail(request):
    context = {
    }
    return render(request, 'consumption/detail.html', context)

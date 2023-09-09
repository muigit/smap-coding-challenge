from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    # ここにアプリケーションごとの設定を記載する
    path('', views.IndexView.as_view(), name='index'),
]

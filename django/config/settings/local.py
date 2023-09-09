# runserverコマンドで起動したローカルサーバを想定しているので、DEBUGは有効、ALLOWED_HOSTSはすべて許可にしています。
# DATABASEの設定はsqliteを使うことを想定していますが、適宜ご自分の環境に変更してください。
# なお、USER、PASSWORDに設定しているos.environ['XXX']は環境変数からの読み出しになります。
# STATICFILES_DIRSはrunseverコマンド実行したときに静的ファイル自動配信機能を読み取りをするディレクトリを指定します。staticディレクトリを設定します。
import os
from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static/')]

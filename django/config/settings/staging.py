# stagingなので、DEBUGは有効、ALLOWED_HOSTSはすべて許可にしています。
# DATABASEはPostgreSQLを想定していまが、適宜ご自分の環境に変更してください。
# なお、os.environ['XXX']は環境変数からの読み出しになります。
# STATIC_ROOTはWebサーバ側でstaticファイルを返すために、staticディレクトリを設定します。
import os
from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ['DB_NAME'],
        'PORT': os.environ['DB_PORT']
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

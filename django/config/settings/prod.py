# 基本はstaging環境と同じですが、DEBUGの設定を削除することで、「base.py」の設定内容であるDEBUG=Falseとしています。
import os
from .base import *

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

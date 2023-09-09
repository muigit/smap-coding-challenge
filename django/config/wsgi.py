"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

# 環境変数を読み込む
load_dotenv('../.env')

envstate = os.getenv('ENV_STATE','local')
if envstate=='production':
    # settings/production.py
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')
elif envstate=='staging':
    # settings/staging.py
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.staging')
else:
    # settings/local.py
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')

application = get_wsgi_application()

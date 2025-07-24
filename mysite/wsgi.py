# mysite/wsgi.py

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()

# ✅ Run create_db after application is loaded
try:
    from create_db import create_tables
    create_tables()
except Exception as e:
    print(f"⚠️ Failed to create DB tables: {e}")

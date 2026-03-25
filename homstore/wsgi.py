import os
from django.core.wsgi import get_wsgi_application

# ระบุชื่อโฟลเดอร์ homstore ตามด้วยจุด . และ settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homstore.settings')

application = get_wsgi_application()
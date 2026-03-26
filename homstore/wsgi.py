import os
from django.core.wsgi import get_wsgi_application

# บอก Django ว่าไฟล์ settings อยู่ในโฟลเดอร์ homstore
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homstore.settings')

application = get_wsgi_application()
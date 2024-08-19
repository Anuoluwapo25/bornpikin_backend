from django.core.wsgi import get_wsgi_application
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")
application = get_wsgi_application()

from django.contrib.auth import get_user_model
User = get_user_model()
print(User.objects.all())
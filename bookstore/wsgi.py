import os
import sys

# Caminho para sua pasta do projeto
project_path = '/home/Michaelmp/bookstoremp'
if project_path not in sys.path:
    sys.path.insert(0, project_path)

# Caminho do virtualenv
activate_env = '/home/Michaelmp/.virtualenvs/bookstoremp/bin/activate_this.py'
with open(activate_env) as file_:
    exec(file_.read(), dict(__file__=activate_env))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstoremp.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

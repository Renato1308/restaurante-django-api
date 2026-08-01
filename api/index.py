import os
import sys

# Caminho da raiz do projeto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

# Configuração do Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

# Inicializa a aplicação WSGI
from django.core.wsgi import get_wsgi_application

app = get_wsgi_application()
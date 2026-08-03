"""
Django settings for core project.
Configurado para desenvolvimento local e deploy de produção na Render.
"""

import os
from pathlib import Path
import dj_database_url

# Base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Segurança - Em produção na Render usa a variável de ambiente, localmente usa a chave padrao
SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    'django-insecure-p^50&=33dttjwse&*!=e%$6m@!14oxk0%%=4c*ix7ypkkt+1yv',
)

# DEBUG somente em desenvolvimento local
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# Hosts permitidos (Aceita localhost, Render e qualquer domínio personalizado)
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.onrender.com',
]

# Se a Render fornecer um HOST específico via variável de ambiente, adiciona automaticamente
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Aplicações
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website',
]

# Middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Servidor de arquivos estáticos
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# Banco de Dados
# Em produção (Render), usa a DATABASE_URL do PostgreSQL se existir.
# Em desenvolvimento local, usa o SQLite.
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}", conn_max_age=600
    )
}

# Validação de senha
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internacionalização
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True
USE_TZ = True

# ==========================
# ARQUIVOS ESTÁTICOS (CSS, JS, Imagens de tema)
# ==========================

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

# Armazenamento otimizado e compactado do WhiteNoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# WhiteNoise
WHITENOISE_AUTOREFRESH = DEBUG
WHITENOISE_USE_FINDERS = DEBUG

# ==========================
# ARQUIVOS DE MÍDIA (Uploads dos Pratos)
# ==========================

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Chave primária padrão
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Força o Django a adicionar a barra no final das URLs automaticamente.
APPEND_SLASH = True
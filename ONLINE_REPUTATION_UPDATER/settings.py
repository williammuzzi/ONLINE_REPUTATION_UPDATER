import os
from pathlib import Path

# BASE DIR - Percorso della cartella del progetto
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-tua-chiave-segreta"

# DEBUG MODE - Attiva solo in sviluppo
DEBUG = False  # Cambia in False in produzione!

# Imposta i domini consentiti (modifica per la produzione)
ALLOWED_HOSTS = ['online-reputation-updater.azurewebsites.net']

# APPLICAZIONI INSTALLATE
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "updater",  # Mantieni il nome dell'app
]

# MIDDLEWARE - Funzioni che processano le richieste HTTP
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Aggiunto per servire i file statici su Azure
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# URL ROOT - Il file principale delle URL
ROOT_URLCONF = "ONLINE_REPUTATION_UPDATER.urls"

# TEMPLATE SETTINGS
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],  # Lascia vuoto, Django troverà i template in ogni app
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# WSGI - Configurazione del server WSGI
WSGI_APPLICATION = "ONLINE_REPUTATION_UPDATER.wsgi.application"

# DATABASE - Configurazione di MySQL
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "subscription",  # Nome del database
        "USER": os.getenv("DB_USER", "william.muzzi@csiportaleu.mysql.database.azure.com"),
        "PASSWORD": os.getenv("DB_PASSWORD", "T9d#1JpY"),
        "HOST": "csiportaleu.mysql.database.azure.com",
        "PORT": "3306",
        "OPTIONS": {
            "ssl": {"ssl-mode": "REQUIRED"}
        }
    }
}

# PASSWORD VALIDATORS - Migliora la sicurezza degli account Django
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# LOCALIZZAZIONE
LANGUAGE_CODE = "it-it"  # Imposta la lingua italiana
TIME_ZONE = "Europe/Rome"
USE_I18N = True
USE_TZ = True

# FILE STATICI (CSS, immagini, JS)
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "updater", "static")]

# MEDIA FILES (file caricati dagli utenti, es. immagini)
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# DEFAULT AUTO FIELD
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

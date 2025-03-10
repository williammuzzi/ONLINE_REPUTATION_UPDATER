import os
from pathlib import Path

# BASE DIR - Percorso della cartella del progetto
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "django-insecure-tua-chiave-segreta")

# DEBUG MODE - Attiva solo in sviluppo
DEBUG = os.getenv("DJANGO_DEBUG", "False") == "True"

# Imposta i domini consentiti (modifica per la produzione)
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "online-reputation-updater.azurewebsites.net").split(",")

# APPLICAZIONI INSTALLATE
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "updater",  # Mantieni il nome dell'app
    "django.contrib.sites",  # Necessario per allauth
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.microsoft",
]

SOCIALACCOUNT_PROVIDERS = {
    "microsoft": {
        "APP": {
            "client_id": os.getenv("MICROSOFT_CLIENT_ID"),
            "secret": os.getenv("MICROSOFT_CLIENT_SECRET"),
            "key": ""
        },
        "SCOPE": ["email", "profile", "openid"],
    }
}

# MIDDLEWARE - Funzioni che processano le richieste HTTP
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Aggiunto per servire i file statici su Azure
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

CSRF_TRUSTED_ORIGINS = [
    'https://online-reputation-ggenhgg2a0a8crhp.northeurope-01.azurewebsites.net',
    'http://online-reputation-ggenhgg2a0a8crhp.northeurope-01.azurewebsites.net'
]

SITE_ID = 1
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]
LOGIN_REDIRECT_URL = "/"
ACCOUNT_LOGOUT_REDIRECT_URL = "/"
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False

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
        "NAME": os.getenv("DB_NAME", "subscription"),
        "USER": os.getenv("DB_USER", "william.muzzi@csiportaleu.mysql.database.azure.com"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST", "csiportaleu.mysql.database.azure.com"),
        "PORT": os.getenv("DB_PORT", "3306"),
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
STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = "/static/"

# WhiteNoise per servire i file statici
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "updater", "static")]

# MEDIA FILES (file caricati dagli utenti, es. immagini)
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# DEFAULT AUTO FIELD
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

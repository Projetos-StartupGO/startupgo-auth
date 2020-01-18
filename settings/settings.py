"""
Django settings for startup_go_auth project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from decouple import config, Csv
from dj_database_url import parse as db_url


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DJANGO_DEBUG", default=False)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv(), default="*")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "oauth2_provider",
    "apps.oauth2",
    "corsheaders",
    "apps.users",
    "crispy_forms",
]

if DEBUG:
    INSTALLED_APPS += ["django_extensions"]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "oauth2_provider.middleware.OAuth2TokenMiddleware",
]

CRISPY_TEMPLATE_PACK = "bootstrap4"


ROOT_URLCONF = "project.urls"

TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATE_DIR],
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
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "oauth2_provider.backends.OAuth2Backend",
]

WSGI_APPLICATION = "project.wsgi.application"

_DEFAULT_DB = "sqlite:///" + os.path.join(BASE_DIR, "db.sqlite3")

DATABASES = {"default": config("DATABASE_URL", default=_DEFAULT_DB, cast=db_url)}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = "/static/"
# STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "static")
AUTH_USER_MODEL = "users.User"
CORS_ORIGIN_ALLOW_ALL = True

JWT_ID_ATTRIBUTE = "id"
JWT_ISSUER = "auth.startupgo.com.br"
JWT_PAYLOAD_ENRICHER = "apps.oauth2.utils.payload_enricher"
JWT_PRIVATE_KEY_RSA = """{
    "p": "1SxHtTgcX_A-NVO8AyomSI_WF5gk0b3MrKCGNp4XBad4OHqHZoHvIcMKKEPCDXu78J93itI7y4ZzsWDF1ZDj1HRWbfWwkep-hDTyH7D8PGy_r_Mvf10Rh5ZkyWwbc-eXNfGOyMntr3ZcccSE_94ibIi4Fby_0J1VHjpY9A6q_-U",
    "kty": "RSA",
    "q": "sbPEkP2WE9RASznNr7uH-WdeunnY8iUEcE-qCGsQXi796eRrTC_V_KFV254KBizUplrsqC2BTCswqGId3AQ3nItQbRsnD0kgZa3aM0S1ikDwdSu_OxVNfz3LSF_aeF_4anh3Cc5yv8FNN6kZoZlrUzCNATvXSuB7kWjnfMS7Pg8",
    "d": "b7pzAxjc3gOSptRijmWL7scQkTnHDnG9pJcWA6K0kACfgXrZbgGu34bqUMuvyImmL_Lt3-LWxgCJFssrej-OwBQfff4INj_k97KXpPkJWIKAxsCs0QIQ56dyLr5J-uOtuUsf4YT02KlzRyBA3LVc_EJLqlKxfoUZcZ8LDjuQQE4mTynMG_btwbPyOGknoIk7alfWTO25872peObF1mq-6WvfXtiAAUCLSz8cQLLuVHms6vFID3tUld878-TZh1pm5AXieyGdqIEs2Tq7Xgwl3dVodeIkNZdhRXbbByb7oWL4200QxWwfWHTD0LBQNbArFi-Z3psujoYvl7WHvrOjoQ",
    "e": "AQAB",
    "use": "sig",
    "qi": "NPOW6S3f8druqchZDxoCyzUE9TXVi6dihk0vCHQl0WgcnnMAZgxRb7ejKzYKEthw7e8yo8KevzzWiqGFZL-h0VA-z78BF5VHzC_tAodHlKK0Q9lFc3Jla7bi8NANZ8VYDWepeFz98S2721aJ4mf2G6zfurP4oG2b3jqm5JRWCA4",
    "dp": "KHrhHxOJp9o6JexBrqQpYuwVbqOQklelbz6IXgTFQGid1rPF1HxmCZY87op3ZhISDU5q5-ymOC7O92b2CmkaKnTxGK5oGj1aSwa217fHHj5UZDgc0-W7d3DisLEbwXW_7Blz0MMvpHsocN4tl1z6Unvf4RjXn-jQig3waGAErtU",
    "alg": "RS256",
    "dq": "eXXxZlUeToFmTMS-tV4N68fe9MCyK5hnt0iMZOKhNm8SONtbB6Eut1WjNNCJ83yTAP3nAnDQDrr6sC0YUblENaj3mQvVH9qQ3U7-dMqC93O5p6z2MbE23kDjgJ2b22llh4i9fKNyxWSfnerkTRNrS1pFFtHLLy_O5i35A8wIW7s",
    "n": "k_lPORJ6qmSdkruoBn-RMAuVwsJa-FOqHPQ9JJG5nVGM_v-KAn_UIsuNJjXuLxsfZoA_VjvWvcw4Uwtp9VZ7yXd2MR0bRot9wKzpdmQwg4G8DIGklaZoI42oKsv1njCspsDJibMC8mVA1f1Z5dWLq1F4W1_PavUtVT1BpYVHhCrdi-3fJO4pex-keo8EavjrduG39X8SzFIqEjsKr-0fsdkoMyjowUsCRLnyX9EUYTFYMnDhE78EdIMlm-grvNFZcPP5DlbBGfRn3CyNXGotCf-O3Hpw-7ZTsGjFvNLHbRzUktxvluQxvWfg367miCGWc8YtKnzlCOvOO4qahkV0aw"
}"""

JWT_PUBLIC_KEY = {
    "kty": "RSA",
    "e": "AQAB",
    "use": "sig",
    "alg": "RS256",
    "n": "k_lPORJ6qmSdkruoBn-RMAuVwsJa-FOqHPQ9JJG5nVGM_v-KAn_UIsuNJjXuLxsfZoA_VjvWvcw4Uwtp9VZ7yXd2MR0bRot9wKzpdmQwg4G8DIGklaZoI42oKsv1njCspsDJibMC8mVA1f1Z5dWLq1F4W1_PavUtVT1BpYVHhCrdi-3fJO4pex-keo8EavjrduG39X8SzFIqEjsKr-0fsdkoMyjowUsCRLnyX9EUYTFYMnDhE78EdIMlm-grvNFZcPP5DlbBGfRn3CyNXGotCf-O3Hpw-7ZTsGjFvNLHbRzUktxvluQxvWfg367miCGWc8YtKnzlCOvOO4qahkV0aw",
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


import os
import environ
from pathlib import Path
import dj_database_url

env = environ.Env(DEBUG=(bool, True))
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(BASE_DIR / ".env", overwrite=True)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(" ")


# Application definition
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.gis",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "djoser",
    "phonenumber_field",
    "rest_framework_gis",
    "corsheaders",
    "whitenoise",
    "oauth2_provider",
    "social_django",
    "drf_social_oauth2",
]

LOCAL_APPS = [
    "apps.users",
    "apps.donation_management",
    "apps.mosque_management",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "oauth2_provider.middleware.OAuth2TokenMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     "default": dj_database_url.config(
#         default=os.environ.get("DATABASE_URL"), conn_max_age=600, engine=os.environ.get("POSTGRES_ENGINE")
#     )
# }


DATABASES = {
    "default": {
        "ENGINE": env("MYSQL_ENGINE"),
        "NAME": env("MYSQL_NAME"),
        "USER": env("MYSQL_USER"),
        "PASSWORD": env("MYSQL_PASSWORD"),
        "HOST": env("MYSQL_HOST"),
        "PORT": env("MYSQL_PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "oauth2_provider.contrib.rest_framework.OAuth2Authentication",
        "drf_social_oauth2.authentication.SocialAuthentication",
    ),
}

OAUTH2_PROVIDER = {
    "SCOPES": {
        "read": "Read access",
        "write": "Write access",
        "groups": "Access to your groups",
    }
}

AUTHENTICATION_BACKENDS = (
   "drf_social_oauth2.backends.DjangoOAuth2",
   "django.contrib.auth.backends.ModelBackend",
)
# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "/staticfiles/"

STATICFILE_DIR = []
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
MEDIA_URL = "/mediafiles/"
MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")  # BASE_DIR / "mediafiles"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "users.User"

from datetime import timedelta

DATE_FORMAT = "%Y-%m-%d"
DATETIME_FORMAT = "%Y-%m-%d %H:%M"

# SIMPLE_JWT = {
#     "AUTH_HEADER_TYPES": (
#         "Bearer",
#         "JWT",
#     ),
#     "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
#     "REFRESH_TOKEN_LIFETIME": timedelta(days=2),
#     "ROTATE_REFRESH_TOKENS": False,
#     "SIGNING_KEY": env("SIGNING_KEY"),
#     "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
#     "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
#     "UPDATE_LAST_LOGIN": True,
#     "AUTH_COOKIE": "refresh_token",  # Cookie name. Enables cookies if value is set.
#     "AUTH_COOKIE_DOMAIN": None,  # A string like "example.com", or None for standard domain cookie.
#     "AUTH_COOKIE_SECURE": False,  # Whether the auth cookies should be secure (https:// only).
#     "AUTH_COOKIE_HTTP_ONLY": True,  # Http only cookie flag.It's not fetch by javascript.
#     "AUTH_COOKIE_PATH": "/",  # The path of the auth cookie.
#     "AUTH_COOKIE_SAMESITE": None,  # Whether to set the flag restricting cookie leaks on cross-site requests.
# }

DJOSER = {
    "LOGIN_FIELD": "email",
    "USER_CREATE_PASSWORD_RETYPE": True,
    "USERNAME_CHANGED_EMAIL_CONFIRMATION": True,
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    "SEND_CONFIRMATION_EMAIL": True,
    "SEND_ACTIVATION_EMAIL": False,
    "PASSWORD_RESET_CONFIRM_URL": "auth/password/reset/confirm/{uid}/{token}",
    "LOGOUT_ON_PASSWORD_CHANGE": False,
    "SET_PASSWORD_RETYPE": True,
    "PASSWORD_RESET_CONFIRM_RETYPE": True,
    "SERIALIZERS": {
        "user_create": "apps.users.serializers.CreateUserSerializer",
        "user": "apps.users.serializers.UserSerializer",
        "current_user": "apps.users.serializers.UserSerializer",
        "user_delete": "djoser.serializers.UserDeleteSerializer",
    },
    "EMAIL": {
        "confirmation": "apps.users.email.ConfirmationEmail",
        "password_reset": "apps.users.email.PasswordResetEmail",
        "password_changed_confirmation": "apps.users.email.PasswordChangedConfirmationEmail",
    },
}


PHONENUMBER_DEFAULT_REGION = "GH"
LOGIN_URL = "/admin/login/"

from .base import *

# Security
SECRET_KEY = config("SECRET_KEY")

# Debug
DEBUG = config("DEBUG", default=False, cast=bool)

# Allowed Hosts
ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

# CORS allowed origins
CORS_ALLOWED_ORIGINS = config("CORS_ALLOWED_ORIGINS", cast=Csv())

# Email
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "'smtp.mailgun.org'"
EMAIL_PORT = 587
EMAIL_HOST_USER = config("EMAIL_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_PASSWORD")
EMAIL_USE_TLS = True

# Media and Static for production use whitenoise
# MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware'] # If you want to use whitenoise instead of nginx

MEDIA_ROOT = os.path.join(BASE_DIR, "../", "media") # store user uploaded files for production

# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage" # If you want to use whitenoise instead of nginx



# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USERNAME"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOSTNAME"),
        "PORT": config("DB_PORT", cast=int),
    }
}

# Caching(No need of caching in development)
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": config("REDIS_BACKEND"),
    },
}
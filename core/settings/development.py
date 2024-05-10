from .base import *

# CORS allowed origins
CORS_ALLOW_ALL_ORIGINS = True

# Email
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Media and Static files(you don't this for production, as you may use other services like AWS S3, Google Cloud Storage, etc.)
MEDIA_ROOT = os.path.join(BASE_DIR, "../", "media_dev") # store user uploaded files for development

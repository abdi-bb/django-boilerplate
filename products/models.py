import uuid
from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    code = models.CharField(blank=True, max_length=12)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
    
    def save(self, *args, **kwargs):
        if not self.code:
            self.code = str(uuid.uuid4()).replace('-', '').upper()[:12]
        super().save(*args, **kwargs)
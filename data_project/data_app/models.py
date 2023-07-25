from django.db import models
from django.utils.crypto import get_random_string
from django.db.models import JSONField

class Account(models.Model):
    email = models.EmailField(unique=True)
    account_id = models.CharField(max_length=50, unique=True)
    account_name = models.CharField(max_length=100)
    app_secret_token = models.CharField(max_length=100, unique=True, editable=False)
    website = models.URLField(blank=True)

    def save(self, *args, **kwargs):
        if not self.app_secret_token:
            self.app_secret_token = get_random_string(length=32)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.account_name


class Destination(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='destinations')
    url = models.URLField()
    http_method = models.CharField(max_length=10)
    headers = models.JSONField()

    def __str__(self):
        return self.url

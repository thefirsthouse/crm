from django.db import models


class Client(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    birthday = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

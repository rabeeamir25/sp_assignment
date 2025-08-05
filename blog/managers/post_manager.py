from django.db import models
from django.utils import timezone
from datetime import timedelta

class PostManager(models.Manager):
    def active(self):
        return self.filter(is_active=True)

    def get_recent_items(self, days=7):
        recent_date = timezone.now() - timedelta(days=days)
        return self.filter(created_at__gte=recent_date)
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from django.utils.text import slugify
import logging
from blog.models.post import Post

logger = logging.getLogger(__name__)

@receiver(pre_save, sender=Post)
def auto_generate_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)

@receiver(post_delete, sender=Post)
def log_post_deletion(sender, instance, **kwargs):
    logger.warning(f"Post deleted: {instance.title} by {instance.author}")
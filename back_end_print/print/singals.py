from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.utils import timezone
from .models import Users

@receiver(user_logged_in)
def update_last_login(sender, user, **kwargs):
    user.last_login = timezone.now()
    user.save(update_fields=['last_login'])
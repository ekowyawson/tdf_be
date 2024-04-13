from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return self.username
    
class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.UUIDField(default=uuid.uuid4, editable=False)
    provider = models.CharField(max_length=255, null=False)
    provider_account_id = models.CharField(max_length=255, null=False)
    refresh_token = models.CharField(max_length=255, null=False)
    access_token = models.CharField(max_length=255, null=False)
    expires_at = models.IntegerField(null=False)
    token_type = models.CharField(max_length=255, null=False)
    scope = models.CharField(max_length=255, null=False)
    id_token = models.CharField(max_length=255, null=False)
    session_state = models.CharField(max_length=255, null=False)

    def to_account_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "provider": self.provider,
            "provider_account_id": self.provider_account_id,
            "refresh_token": self.refresh_token,
            "access_token": self.access_token,
            "expires_at": self.expires_at,
            "token_type": self.token_type,
            "scope": self.scope,
            "id_token": self.id_token,
            "session_state": self.session_state,
        }
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('TN', 'Tenant'),
        ('SV', 'Service Professional'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='register_profile')
    # Add additional fields for the user profile

    def __str__(self):
        return self.user.username

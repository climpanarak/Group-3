from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import uuid



class UserProfile(models.Model):
    """Model representing a user profile."""
    ROLE_CHOICES = (
        ('MP', 'Management Property'),
        ('PO', 'Property Owner'),
        ('TN', 'Tenant'),
        ('SV', 'Service Professional')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=2, choices=ROLE_CHOICES)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.user.username} - {self.get_role_display()}'

class Property(models.Model):
    """Model representing a property."""
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    property_image = models.ImageField(upload_to='images/', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('property_detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Room(models.Model):
    """Model representing a room."""
    PROPERTY_CHOICES = (
        ('MB', 'Master Bedroom'),
        ('NR', 'Normal Room'),
    )
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=PROPERTY_CHOICES)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.get_type_display()} - {self.property}'

class Invoice(models.Model):
    """Model representing an invoice."""
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    invoice = models.FileField(upload_to='Invoice', blank=True)

    def get_absolute_url(self):
        return reverse('index')

class Application(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    property = models.ForeignKey(Property, on_delete=models.CASCADE, null=True)
from django.contrib import admin
from .models import Property, Room, UserProfile

admin.site.register(Property)
admin.site.register(UserProfile)
admin.site.register(Room)

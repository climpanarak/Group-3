from django.contrib import admin
from .models import Property, Room, UserProfile, Application, Invoice

admin.site.register(Property)
admin.site.register(UserProfile)
admin.site.register(Room)
admin.site.register(Invoice)
admin.site.register(Application)
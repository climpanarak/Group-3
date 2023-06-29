from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileField(forms.ModelChoiceField):
    def label_from_instance(self, user_profile):
        return user_profile.user.username

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    role = forms.ChoiceField(choices=UserProfile.ROLE_CHOICES)

    class Meta:
        model = User
        fields = ["username","first_name", "last_name", "email", "password1", "password2"]
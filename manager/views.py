from .models import Property, Room
from django.shortcuts import render
from .models import Property, Room
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    """View function for home page of site."""
    num_properties = Property.objects.all().count()
    num_rooms = Room.objects.all().count()

    context = {
        'num_properties': num_properties,
        'num_rooms': num_rooms,
    }

    return render(request, 'catalog/index.html', context=context)

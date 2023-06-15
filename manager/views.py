from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Property, Room
from django.shortcuts import render, redirect
from django.db.models import Q

def index(request):
    """View function for home page of site."""
    num_properties = Property.objects.all().count()
    num_rooms = Room.objects.all().count()

    context = {
        'num_properties': num_properties,
        'num_rooms': num_rooms,
    }

    return render(request, 'manager/index.html', context=context)

class PropertyListView(LoginRequiredMixin, generic.ListView):
    model = Property

class PropertyDetailView(LoginRequiredMixin, generic.DetailView):
    model = Property

def property_search(request):
    query = request.GET.get('query')
    properties = []

    if query:
        properties = Property.objects.filter(Q(name__icontains=query))

    context = {'properties': properties}
    return render(request, 'manager/property_search.html', context)
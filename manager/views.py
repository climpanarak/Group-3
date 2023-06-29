from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Property, Room, Application
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

class ApplicationCreate(CreateView):
    model = Application
    fields = ['name', 'email','property']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return HttpResponseRedirect(reverse('application_list'))

class ApplicationListView(LoginRequiredMixin, generic.ListView):
    model = Application

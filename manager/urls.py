from django.urls import path
from . import views
from .views import property_search

urlpatterns = [
    path('', views.index, name='index'),
    path('property_list/', views.PropertyListView.as_view(), name='property_list'),
    path('property_detail/<int:pk>', views.PropertyDetailView.as_view(), name='property_detail'),
    path('search/', property_search, name='property_search'),
    path('submit/', views.submit_applicationDetailView.as_view(), name='submit_application'),
    path('application/', views.ApplicationListView.as_view(), name='application_form'),
]
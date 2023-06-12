from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('property_list/', views.PropertyListView.as_view(), name='property_list'),
]
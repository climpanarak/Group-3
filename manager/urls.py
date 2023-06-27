from django.urls import path
from . import views
from .views import property_search

urlpatterns = [
    path('', views.index, name='index'),
    path('property_list/', views.PropertyListView.as_view(), name='property_list'),
    path('property_detail/<int:pk>', views.PropertyDetailView.as_view(), name='property_detail'),
    path('invoice', views.InvoiceView.as_view(), name='invoice'),
    path('search/', property_search, name='property_search')
]
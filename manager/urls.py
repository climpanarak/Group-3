from django.urls import path
from . import views
from .views import property_search

urlpatterns = [
    path('', views.index, name='index'),
    path('property_list/', views.PropertyListView.as_view(), name='property_list'),
    path('property_detail/<int:pk>', views.PropertyDetailView.as_view(), name='property_detail'),
    path('invoice/create', views.InvoiceCreate.as_view(), name='invoice_create'),
    path('invoice/<int:pk>/update/', views.InvoiceUpdate.as_view(), name='invoice_update'),
    path('search/', property_search, name='property_search')
]
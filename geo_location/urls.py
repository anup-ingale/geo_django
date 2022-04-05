from django.urls import path
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name ='index.html'), name='home'),
    path('cities_data/',cities_data, name='cities_data'),
    path('forcasted_data/',forcast_data, name='forcasted_data')
]
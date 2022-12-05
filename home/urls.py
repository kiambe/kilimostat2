from django.urls import path

from . import views



urlpatterns = [
    path('', views.index, name='home'),
    path('data/', views.datadownload, name='data'),
    path('covid19/', views.covid19, name='covid19'),
]

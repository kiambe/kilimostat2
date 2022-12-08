from django.urls import path

from . import views



urlpatterns = [
    path('', views.index, name='home'),
    path('data/', views.datadownload, name='data'),
    path('covid19/', views.covid19, name='covid19'),
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),
    path('terms/', views.terms, name='terms'),
    path('policy/', views.policy, name='policy'),
    path('census/', views.census, name='census'),
    path('definitions/', views.definitions, name='definitions'),
    path('metadata/', views.metadata, name='metadata'),
]

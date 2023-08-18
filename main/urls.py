from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('pokaz', views.pokaz, name='pokaz')
]

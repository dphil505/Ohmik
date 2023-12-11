from django.urls import path
from . import views


urlpatterns = [
    path("", views.main, name="main"),
    path("home", views.home, name='home'),
    path("cellTrack", views.cellTrack, name='cellTrack'),
    path('supplierRegit', views.supplierRegit, name='supplierRegit'),
    path('modelRegit', views.modelRegit, name='modelRegit')
]
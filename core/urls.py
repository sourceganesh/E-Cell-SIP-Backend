from django.urls import path
from core import views

urlpatterns = [
    path('', views.startup_form, name= 'startupform')
]
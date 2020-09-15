from django.urls import path
from core import views

urlpatterns = [
    path('', views.startup_form, name= 'startupform'),
    path('view', views.student_intership_view, name= 'student_intership_view')
]
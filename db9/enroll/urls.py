from django.urls import path 
from . import views

urlpatterns = [
    path('', views.showForm),
    path('success/',views.success, name='success')
]

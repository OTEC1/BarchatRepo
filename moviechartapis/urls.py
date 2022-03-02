from django.urls import path
from . import views

urlpatterns = [
    path('', views.barchart, name='chart-home')
]
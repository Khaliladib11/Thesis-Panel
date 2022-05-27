from django.urls import path
from . import views

urlpatterns = [
    path('', views.theses, name="theses"),
    path('thesis/<str:pk>', views.thesis, name="thesis"),
]
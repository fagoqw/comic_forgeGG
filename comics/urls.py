# comics/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_comic, name='create_comic'),
    path('', views.view_comics, name='view_comics'),
]

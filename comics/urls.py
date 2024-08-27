from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_comic, name='create_comic'),
    path('comics/', views.view_comics, name='view_comics'),
    path('comics/<int:comic_id>/', views.detail_comic, name='detail_comic'),
    path('comics/<int:comic_id>/delete/', views.delete_comic, name='delete_comic'),
    path('search/', views.search_comics, name='search_comics'),
    path('comics/<int:comic_id>/upload_images/', views.upload_images, name='upload_images'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

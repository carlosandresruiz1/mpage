from django.urls import path
from SongApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('artist/', views.ArtistApi),
    path('artist/<int:id>', views.ArtistApi),
    path('user/', views.UserApi),
    path('user/<int:id>', views.UserApi),
    path('album/', views.AlbumApi),
    path('album/<int:id>', views.AlbumApi),
    path('song/', views.SongApi),
    path('song/<int:id>', views.SongApi),
    path('usersong/', views.UserSongApi),
    path('usersong/<int:id>', views.UserSongApi),
    path('useralbum/', views.UserAlbumApi),
    path('useralbum/<int:id>', views.UserAlbumApi),  
    path('rol/', views.RolApi),
    path('rol/<int:id>', views.RolApi),
    path('songartist/', views.ArtistRolSongApi),
    path('songartist/<int:id>', views.ArtistRolSongApi),
    path('savefile', views.save_file)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
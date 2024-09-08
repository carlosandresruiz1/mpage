from django.contrib import admin

from .models import Song,Album,Artist,User,UserSong,UserAlbum,Rol,ArtistRolSong

# Register your models here.

admin.site.register(Song)
admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(User)
admin.site.register(UserSong)
admin.site.register(UserAlbum)
admin.site.register(Rol)
admin.site.register(ArtistRolSong)


from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from SongApp.models import Artist, ArtistRolSong, User, Album, Song, UserSong, UserAlbum, Rol
from SongApp.serializers import ArtistSerializer, UserSerializer, AlbumSerializer, SongSerializer, UserSongSerializer, UserAlbumSerializer, ArtistRolSongSerializer, RolSerializer

from django.core.files.storage import default_storage

# Create your views here.


@csrf_exempt
def ArtistApi(request, id=0):
    if request.method == 'GET':
        artists = Artist.objects.all()
        artist_serializer = ArtistSerializer(artists, many=True)
        return JsonResponse(artist_serializer.data, safe=False)
    elif request.method == 'POST':
        artist_data = JSONParser().parse(request)
        artist_serializer = ArtistSerializer(data=artist_data)
        if artist_serializer.is_valid():
            artist_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        artist_data = JSONParser().parse(request)
        artist = Artist.objects.get(artist_id=artist_data['artist_id'])
        artist_serializer = ArtistSerializer(artist, data=artist_data)
        if artist_serializer.is_valid():
            artist_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        artist = Artist.objects.get(artist_id=id)
        artist.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    
@csrf_exempt    
def UserApi(request, id=0):
    if request.method == 'GET':
        users = User.objects.all()
        user_serializer = UserSerializer(users, many=True)
        return JsonResponse(user_serializer.data, safe=False)
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user = User.objects.get(user_id=user_data['user_id'])
        user_serializer = UserSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        user = User.objects.get(user_id=id)
        user.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    

@csrf_exempt 
def AlbumApi(request, id=0): 
    if request.method == 'GET':
        albums = Album.objects.all()
        album_serializer = AlbumSerializer(albums, many=True)
        return JsonResponse(album_serializer.data, safe=False)
    elif request.method == 'POST':
        album_data = JSONParser().parse(request)
        album_serializer = AlbumSerializer(data=album_data)
        if album_serializer.is_valid():
            album_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        album_data = JSONParser().parse(request)
        album = Album.objects.get(album_id=album_data['album_id'])
        album_serializer = AlbumSerializer(album, data=album_data)
        if album_serializer.is_valid():
            album_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        album = Album.objects.get(album_id=id)
        album.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt 
def SongApi(request, id=0):
    if request.method == 'GET':
        songs = Song.objects.all()
        song_serializer = SongSerializer(songs, many=True)
        return JsonResponse(song_serializer.data, safe=False)
    elif request.method == 'POST':
        song_data = JSONParser().parse(request)
        song_serializer = SongSerializer(data=song_data)
        if song_serializer.is_valid():
            song_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        song_data = JSONParser().parse(request)
        song = Song.objects.get(song_id=song_data['song_id'])
        song_serializer = SongSerializer(song, data=song_data)
        if song_serializer.is_valid():
            song_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        song = Song.objects.get(song_id=id)
        song.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    

@csrf_exempt 
def UserSongApi(request, id=0):
    if request.method == 'GET':
        user_songs = UserSong.objects.all()
        user_song_serializer = UserSongSerializer(user_songs, many=True)
        return JsonResponse(user_song_serializer.data, safe=False)
    elif request.method == 'POST':
        user_song_data = JSONParser().parse(request)
        user_song_serializer = UserSongSerializer(data=user_song_data)
        if user_song_serializer.is_valid():
            user_song_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        user_song_data = JSONParser().parse(request)
        user_song = UserSong.objects.get(user_song_id=user_song_data['user_song_id'])
        user_song_serializer = UserSongSerializer(user_song, data=user_song_data)
        if user_song_serializer.is_valid():
            user_song_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        user_song = UserSong.objects.get(user_song_id=id)
        user_song.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt 
def UserAlbumApi(request, id=0):
    if request.method == 'GET':
        user_albums = UserAlbum.objects.all()
        user_album_serializer = UserAlbumSerializer(user_albums, many=True)
        return JsonResponse(user_album_serializer.data, safe=False)
    elif request.method == 'POST':
        user_album_data = JSONParser().parse(request)
        user_album_serializer = UserAlbumSerializer(data=user_album_data)
        if user_album_serializer.is_valid():
            user_album_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        user_album_data = JSONParser().parse(request)
        user_album = UserAlbum.objects.get(user_album_id=user_album_data['user_album_id'])
        user_album_serializer = UserAlbumSerializer(user_album, data=user_album_data)
        if user_album_serializer.is_valid():
            user_album_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        user_album = UserAlbum.objects.get(user_album_id=id)
        user_album.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    
@csrf_exempt
def ArtistRolSongApi(request, id=0):
    if request.method == 'GET':
        artist_rol_songs = ArtistRolSong.objects.all()
        artist_rol_song_serializer = ArtistRolSongSerializer(artist_rol_songs, many=True)
        return JsonResponse(artist_rol_song_serializer.data, safe=False)
    elif request.method == 'POST':
        artist_rol_song_data = JSONParser().parse(request)
        artist_rol_song_serializer = ArtistRolSongSerializer(data=artist_rol_song_data)
        if artist_rol_song_serializer.is_valid():
            artist_rol_song_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        artist_rol_song_data = JSONParser().parse(request)
        artist_rol_song = ArtistRolSong.objects.get(artist_rol_song_id=artist_rol_song_data['artist_rol_song_id'])
        artist_rol_song_serializer = ArtistRolSongSerializer(artist_rol_song, data=artist_rol_song_data)
        if artist_rol_song_serializer.is_valid():
            artist_rol_song_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        artist_rol_song = ArtistRolSong.objects.get(artist_rol_song_id=id)
        artist_rol_song.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def RolApi(request, id=0):
    if request.method == 'GET':
        rols = Rol.objects.all()
        rol_serializer = RolSerializer(rols, many=True)
        return JsonResponse(rol_serializer.data, safe=False)
    elif request.method == 'POST':
        rol_data = JSONParser().parse(request)
        rol_serializer = RolSerializer(data=rol_data)
        if rol_serializer.is_valid():
            rol_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        rol_data = JSONParser().parse(request)
        rol = Rol.objects.get(rol_id=rol_data['rol_id'])
        rol_serializer = RolSerializer(rol, data=rol_data)
        if rol_serializer.is_valid():
            rol_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        rol = Rol.objects.get(rol_id=id)
        rol.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    
@csrf_exempt
def AlbumApi(request, id=0):
    if request.method == 'GET':
        if id != 0:
            try:
                album = Album.objects.get(album_id=id)
                album_serializer = AlbumSerializer(album)
                return JsonResponse(album_serializer.data, safe=False)
            except Album.DoesNotExist:
                return JsonResponse("Album not found", safe=False)
        else:
            albums = Album.objects.all()
            album_serializer = AlbumSerializer(albums, many=True)
            return JsonResponse(album_serializer.data, safe=False)
    elif request.method == 'POST':
        album_data = JSONParser().parse(request)
        album_serializer = AlbumSerializer(data=album_data)
        if album_serializer.is_valid():
            album_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        album_data = JSONParser().parse(request)
        album = Album.objects.get(album_id=album_data['album_id'])
        album_serializer = AlbumSerializer(album, data=album_data)
        if album_serializer.is_valid():
            album_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        album = Album.objects.get(album_id=id)
        album.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt 
def SongApi(request, id=0):
    if request.method == 'GET':
        if id != 0:
            try:
                song = Song.objects.get(song_id=id)
                song_serializer = SongSerializer(song)
                return JsonResponse(song_serializer.data, safe=False)
            except Song.DoesNotExist:
                return JsonResponse("Song not found", safe=False)
        else:
            songs = Song.objects.all()
            song_serializer = SongSerializer(songs, many=True)
            return JsonResponse(song_serializer.data, safe=False)
    elif request.method == 'POST':
        song_data = JSONParser().parse(request)
        song_serializer = SongSerializer(data=song_data)
        if song_serializer.is_valid():
            song_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        song_data = JSONParser().parse(request)
        song = Song.objects.get(song_id=song_data['song_id'])
        song_serializer = SongSerializer(song, data=song_data)
        if song_serializer.is_valid():
            song_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        song = Song.objects.get(song_id=id)
        song.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    
@csrf_exempt
def save_file(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    file_url = default_storage.url(file_name)
    return JsonResponse({'file_url': file_url})
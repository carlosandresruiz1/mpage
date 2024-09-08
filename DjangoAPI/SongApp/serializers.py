from rest_framework import serializers
from SongApp.models import Song, Album, Artist, User, UserSong, UserAlbum, Rol, ArtistRolSong


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('artist_id', 
                  'artist_name')
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 
                  'user_name',
                  'user_image')
        
class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('album_id', 
                  'album_name',
                  'album_image',
                  'fk_artist_id',
                  'release_date')
        
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('song_id', 
                  'song_name',
                    'song_url',
                    'song_lyrics_e',
                  'fk_album_id',
                  'fk_artist_id')
        
class UserSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSong
        fields = ('user_song_id', 
                  'fk_user_id',
                  'fk_song_id',
                  'user_like',
                  'user_comment')
    
class UserAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAlbum
        fields = ('user_album_id', 
                  'fk_user_id',
                  'fk_album_id',
                  'user_like',
                  'user_comment')
        
class ArtistRolSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistRolSong
        fields = ('artist_rol_song_id', 
                  'fk_artist_id',
                  'fk_rol_id',
                  'fk_song_id')
class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ('rol_id', 
                  'rol_name')

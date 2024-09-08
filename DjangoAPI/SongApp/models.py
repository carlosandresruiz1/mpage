from django.db import models

# Create your models here.

class Artist(models.Model):
    artist_id = models.AutoField(primary_key=True)
    artist_name = models.CharField(max_length=100)

    def __str__(self):
        return self.artist_name
 

class Rol(models.Model):
    rol_id = models.AutoField(primary_key=True)
    rol_name = models.CharField(max_length=100)

    def __str__(self):
        return self.rol_name

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    user_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.user_name

class Album(models.Model):
    album_id = models.AutoField(primary_key=True)
    album_name = models.CharField(max_length=100)
    album_image = models.ImageField(upload_to='images/')
    fk_artist_id = models.ManyToManyField(Artist)
    release_date = models.DateField()

    def __str__(self):
        return self.album_name

class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    song_name = models.CharField(max_length=100)
    song_url = models.CharField(max_length=200)
    song_lyrics_e = models.CharField(max_length=500)
    fk_almbum_id = models.ForeignKey(Album, on_delete=models.CASCADE)
    fk_artist_id = models.ManyToManyField(Artist)

    def __str__(self):
        return self.song_name

class UserSong(models.Model):
    user_song_id = models.AutoField(primary_key=True)
    fk_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    fk_song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    user_like = models.BooleanField()
    user_comment = models.CharField(max_length=100)


class UserAlbum(models.Model):
    user_album_id = models.AutoField(primary_key=True)
    fk_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    fk_album_id = models.ForeignKey(Album, on_delete=models.CASCADE)
    user_like = models.BooleanField()
    user_comment = models.CharField(max_length=100)

class ArtistRolSong(models.Model):
    artist_rol_song_id = models.AutoField(primary_key=True)
    fk_artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    fk_rol_id = models.ForeignKey(Rol, on_delete=models.CASCADE)
    fk_song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    
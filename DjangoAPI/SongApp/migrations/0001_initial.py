# Generated by Django 5.1 on 2024-09-03 03:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('artist_id', models.AutoField(primary_key=True, serialize=False)),
                ('artist_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ArtistRol',
            fields=[
                ('artist_rol_id', models.AutoField(primary_key=True, serialize=False)),
                ('artist_rol_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=100)),
                ('user_image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('album_id', models.AutoField(primary_key=True, serialize=False)),
                ('album_name', models.CharField(max_length=100)),
                ('album_image', models.ImageField(upload_to='images/')),
                ('release_date', models.DateField()),
                ('fk_artist_id', models.ManyToManyField(to='SongApp.artist')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('song_id', models.AutoField(primary_key=True, serialize=False)),
                ('song_name', models.CharField(max_length=100)),
                ('fk_almbum_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SongApp.album')),
                ('fk_artist_id', models.ManyToManyField(to='SongApp.artist')),
            ],
        ),
        migrations.CreateModel(
            name='UserAlbum',
            fields=[
                ('user_album_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_like', models.BooleanField()),
                ('user_comment', models.CharField(max_length=100)),
                ('fk_album_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SongApp.album')),
                ('fk_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SongApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserSong',
            fields=[
                ('user_song_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_like', models.BooleanField()),
                ('user_comment', models.CharField(max_length=100)),
                ('fk_song_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SongApp.song')),
                ('fk_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SongApp.user')),
            ],
        ),
    ]

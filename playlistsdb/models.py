from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class song(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length = 100)
    artist = models.CharField(max_length = 100)
    album = models.CharField(max_length = 100)

    def __str__(self):
        return self.title

    @classmethod
    def create(cls,title,artist,album):
        song = cls(title=title,artist=artist,album=album)
        return song



class playlist(models.Model):
    playlistid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 100)
    songs =ArrayField(models.CharField(max_length=100),null=True)


    def __str__(self):
        return self.name







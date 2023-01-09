from rest_framework import serializers

from .models import playlist,song

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = playlist
        fields = ('playlistid','name','songs')

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = song
        fields = ('id','title','artist','album')

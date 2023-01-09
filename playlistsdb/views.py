from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import Http404
from .models import playlist,song
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt


from .serializers import PlaylistSerializer,SongSerializer
# Create your views here.

@csrf_exempt
def index(request):
    return HttpResponse("You're at the playlists index.")



class PlaylistView(APIView):
    def get(self,request,format=None,pk=None):
        try:
            data=playlist.objects.all()
            serializer=PlaylistSerializer(data,many=True)
            return Response(serializer.data)
        except :
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self,request,format=None):
        serializer=PlaylistSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response=Response()
        response.data={'message':'Playlist created successfully','data':serializer.data}
        return Response(response.data)

    def put(self,request,pk=None,format=None):
        playlist_to_update=playlist.objects.get(pk=pk)
        serializer=PlaylistSerializer(instance=playlist_to_update,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response=Response()
        response.data={'message':'Playlist updated successfully','data':serializer.data}
        return Response(response.data)

    def delete(self,request,pk=None,format=None):
        playlist_to_delete=playlist.objects.get(pk=pk)
        playlist_to_delete.delete()
        response=Response()
        response.data={'message':'Playlist deleted successfully'}
        return Response(response.data)


class SongsView(APIView):
    def get(self,request,format=None,pk=None):
        if (pk is None):
            data=song.objects.all()
            serializer=SongSerializer(data,many=True)
            return Response(serializer.data)
        else:
            data = song.objects.get(pk = pk)
            serializer = SongSerializer(data)
            return Response(serializer.data)
    def post(self,request,format=None):
        serializer=SongSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response=Response()
        response.data={'message':'Song created successfully','data':serializer.data}
        return Response(response.data)

    def put(self,request,pk=None,format=None):
        song_to_update=song.objects.get(pk=pk)
        serializer=SongSerializer(instance=song_to_update,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response=Response()
        response.data={'message':'Song updated successfully','data':serializer.data}
        return Response(response.data)

    def delete(self,request,pk=None,format=None):
        song_to_delete=song.objects.get(pk=pk)
        song_to_delete.delete()
        response=Response()
        response.data={'message':'Song deleted successfully'}
        return Response(response.data)
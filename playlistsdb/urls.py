from django.urls import path
from .views import PlaylistView,SongsView
from . import views


urlpatterns = [
    path('index',views.index , name = 'index'),
    path('playlists',PlaylistView.as_view()),
    path('playlists/<int:pk>',PlaylistView.as_view()),
    path('songs',SongsView.as_view()),
    path('songs/<int:pk>',SongsView.as_view()),
]



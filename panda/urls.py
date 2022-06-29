from django.urls import path
from . views import getResult, searchMovie, getMovie

urlpatterns = [
    path('search/<str:search>', view=searchMovie, name="search"),
    path('get/<str:link>', view=getMovie, name="get"),
    path('get/<str:link>/result', view=getResult, name="result"),
]

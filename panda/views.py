from telnetlib import DO
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from . serializers import WatchableSerializer, UserSerializer
from django.contrib.auth import authenticate
from . customThreads import *
from knox.models import AuthToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from . models import DownloadLinks
from . utils import generateHash
from rest_framework.generics import RetrieveAPIView
from . serializers import LinkSerializer
from django.shortcuts import redirect


# Create your views here.


# authentication views
class CreateUserView(APIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]
        user = User.objects.create_user(username=username, password=password, email="")
        return Response({
            "Token": AuthToken.objects.create(user)[1]
        })

class LoginView(APIView):
    # this view will allow us to get our token
    # by sending our a POST request
    # the users credentials like a username and password 
    serializer_class = UserSerializer
    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]
        user = authenticate(username=username, password=password)
        if user is None:
            return Response({"Info":" Invalid credentials"})
        return Response({
            "Token": AuthToken.objects.create(user)[1]
        })




@api_view(['GET'])
#@permission_classes([IsAuthenticated])
# here we decorate the view as an api that only perform http get operations
def searchMovie(request, search):
    # this is a view that will start the search for the movie in
    # question and then return a json using the django-rest-framework
    # containing the list of items or articles found from the search
    thread = CustomSearchThread(search=search)
    thread.start()
    thread.join()
    watchables = thread.result
    if watchables != False:
        serializer = WatchableSerializer(watchables, many=True)
        return Response(serializer.data)
    else:
        return Response({"status": "no results found"})


@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def getMovie(request, link):

    download_thread = CustomProcessThread(link=link)
    download_thread.setDaemon(True)
    download_thread.start()
    download_thread.join()
    if download_thread.result != False:
        hash_id = ShortenLink(download_thread.resul.getDownloadLink())
        return redirect("video", hash=hash_id)
        #Response({"download-link": download_thread.result.getDownloadLink()})
    else:
        return Response({"status": "download link in progress"})


# Create your views here.
def ShortenLink(link):
    original_link = link
    print("f{original_link} is the original link")
    link_hash = generateHash()
    Link = DownloadLinks.objects.create(original_link=original_link, hash_value=link_hash)
    Link.save()
    return link_hash

class RetrieveLinkView(RetrieveAPIView):
    queryset = DownloadLinks.objects.all()
    lookup_url_kwarg = "hash"
    serializer_class = LinkSerializer


from rest_framework.response import Response
from rest_framework.decorators import api_view
from . serializers import WatchableSerializer
from rest_framework.renderers import JSONRenderer
from . customThreads import *
# Create your views here.


@api_view(['GET'])
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
        return Response(JSONRenderer().render(serializer.data))
    else:
        return Response({"status": "no results found"})


@api_view(['GET'])
def getMovie(request, link):
    download_thread = CustomProcessThread(link=link)
    download_thread.start()
    download_thread.join()
    watchable_item = download_thread.result
    if watchable_item != False:
        serializer = WatchableSerializer(watchable_item)
        return Response(JSONRenderer().render(serializer.data))
    else:
        return Response({"status": "process failed"})

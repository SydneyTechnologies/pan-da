from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import LinkSerializer
from rest_framework.response import Response

# Create your views here.
class ShortenLink(APIView):
    serializer_class = LinkSerializer
    def get(request, link):
        return Response(link)
from rest_framework import serializers
from django.contrib.auth import get_user_model
from . models import DownloadLinks

class WatchableSerializer(serializers.Serializer):
    # serializes the python class watchable to display into json
    link = serializers.CharField(max_length=200)
    title = serializers.CharField(max_length=200)
    video_spec = serializers.CharField(max_length = 200, required=False)
    description = serializers.CharField(max_length=500)
    image = serializers.CharField(max_length=200)
    downloadLink = serializers.CharField(max_length=200)
    identifier = serializers.CharField(max_length=200)



...
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "password"]



class LinkSerializer(serializers.Serializer):
    class Meta:
        model = DownloadLinks
        fields = ["original_link"]
    
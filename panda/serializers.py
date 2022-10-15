from rest_framework import serializers


class WatchableSerializer(serializers.Serializer):
    # serializes the python class watchable to display into json
    link = serializers.CharField(max_length=200)
    title = serializers.CharField(max_length=200)
    video_spec = serializers.CharField(max_length = 200, required=False)
    description = serializers.CharField(max_length=500)
    image = serializers.CharField(max_length=200)
    downloadLink = serializers.CharField(max_length=200)
    identifier = serializers.CharField(max_length=200)

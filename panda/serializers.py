from rest_framework import serializers


class WatchableSerializer(serializers.Serializer):
    link = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=500)
    image = serializers.CharField(max_length=200)
    downloadLink = serializers.CharField(max_length=200)

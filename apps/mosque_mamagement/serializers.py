from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Coordinates, Mosque, MediaFile, Sermon


class CoordinatesSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Coordinates
        geo_field = "location"
        fields = "__all__"


class MosqueSerializer(serializers.ModelSerializer):
    location = CoordinatesSerializer()

    class Meta:
        model = Mosque
        fields = "__all__"


class MediaFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = ['id', 'title', 'file', 'media_type', 'uploaded_at']

class SermonSerializer(serializers.ModelSerializer):
    audio = MediaFileSerializer(many=True, read_only=True)
    video = MediaFileSerializer(many=True, read_only=True)

    class Meta:
        model = Sermon
        fields = "__all__"
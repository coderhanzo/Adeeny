from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from drf_extra_fields.geo_fields import PointField
from drf_extra_fields.fields import Base64FileField
from .models import Mosque, MediaFile, MediaImage, Sermon, Annoucement
from utils.utils import Base64File
import base64


class MosqueSerializer(serializers.ModelSerializer):
    # location = PointField()
    # certificate = Base64FileField(required=False)
    # image = Base64File(required=False)

    class Meta:
        model = Mosque
        fields = "__all__"


class MediaImageSerializer(serializers.ModelSerializer):
    image = Base64File()

    class Meta:
        model = MediaImage
        fields = "__all__"


class MediaFileSerializer(serializers.ModelSerializer):
    file = Base64File()

    class Meta:
        model = MediaFile
        fields = "__all__"


class SermonSerializer(serializers.ModelSerializer):
    audio = MediaFileSerializer(many=True, read_only=True)
    video = MediaFileSerializer(many=True, read_only=True)

    class Meta:
        model = Sermon
        fields = "__all__"


class AnnoucementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annoucement
        fields = "__all__"

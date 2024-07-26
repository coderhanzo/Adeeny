from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from drf_extra_fields.geo_fields import PointField
from drf_extra_fields.fields import Base64FileField
from .models import Mosque, Sermon, Annoucement
# from utils.utils import Base64File
# from drf_extra_fields.fields import Base64ImageField


class MosqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mosque
        fields = "__all__"

class SermonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sermon
        fields = "__all__"


class AnnoucementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annoucement
        fields = "__all__"

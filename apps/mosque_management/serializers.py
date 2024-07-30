from rest_framework import serializers
from .models import Mosque, Sermon, Annoucement


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

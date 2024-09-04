from rest_framework import serializers
from .models import Mosque, Sermon, Announcement


class MosqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mosque
        fields = "__all__"

class SermonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sermon
        fields = "__all__"
    
class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = "__all__"

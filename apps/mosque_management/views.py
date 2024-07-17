# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from rest_framework.permissions import IsAdminUser, IsAuthenticated 
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from .models import Mosque, MediaImage, MediaFile, Sermon, Annoucement
from .serializers import MosqueSerializer, MediaImageSerializer, MediaFileSerializer, SermonSerializer, AnnoucementSerializer


@api_view(["POST"])
def create_mosque(request):
    serializer = MosqueSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    certificate_data = request.data.get("certificate", None)
    mosque_images_data = request.data.get("image", [])

    with transaction.atomic():
        mosque_instance = serializer.save()

        if certificate_data:
            certificate_serializer = MediaFileSerializer(
                data={"file": certificate_data}
            )
            certificate_serializer.is_valid(raise_exception=True)
            certificate_instance = certificate_serializer.save()
            mosque_instance.certificate = certificate_instance.file
            mosque_instance.save()

        mosque_image_instances = []
        for image_data in mosque_images_data:
            image_serializer = MediaImageSerializer(data={"image": image_data})
            image_serializer.is_valid(raise_exception=True)
            image_instance = image_serializer.save()
            mosque_image_instances.append(image_instance)

        mosque_instance.mosque_image.set(mosque_image_instances)
        mosque_instance.save()

    return Response({"status": "success"}, status=status.HTTP_201_CREATED)


class GetAllMosques(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        mosques = Mosque.objects.all()
        serializer = MosqueSerializer(mosques, many=True)
        return Response(serializer.data)

class GetAndUpdateMosque(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        mosque = self.get_object(pk)
        serializer = MosqueSerializer(mosque)
        return Response(serializer.data)

    def patch(self, request, pk):
        mosque = self.get_object(pk)
        serializer = MosqueSerializer(mosque, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

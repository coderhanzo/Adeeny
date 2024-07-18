from django.shortcuts import render
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.permissions import IsAdminUser
from .models import ProjectDonation
from .serializers import CreateProjectDonationSerializer
# Create your views here.


@api_view(["POST"])
def create_project_donation(request):
  serializer = CreateProjectDonationSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetAllProjectDonation(APIView):
  permission_classes = [IsAdminUser]

  def get(self, request):
    donations = ProjectDonation.objects.all()
    serializer = CreateProjectDonationSerializer(donations, many=True)
    return Response(serializer.data)
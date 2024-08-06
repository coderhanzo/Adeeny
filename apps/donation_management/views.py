from django.shortcuts import render
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework_simplejwt.authentication import (
    JWTAuthentication,
    JWTStatelessUserAuthentication,
)
from .models import ProjectDonation
from .serializers import MonetaryDoantionsSerializer

# Create your views here.


@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def create_project_donation(request):
    serializer = MonetaryDoantionsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetAllProjectDonation(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        donations = ProjectDonation.objects.all()
        serializer = MonetaryDoantionsSerializer(donations, many=True)
        return Response(serializer.data)

# filter donations by date
@api_view(["GET"])
def get_project_donation_by_date(request, date):
    donations = ProjectDonation.objects.filter(date=date)
    serializer = MonetaryDoantionsSerializer(donations, many=True)
    return Response(serializer.data)

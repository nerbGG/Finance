# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from database.models import Profile
from .serializers import ProfileSerializer

# Create your views here.
@api_view(["GET"])
def getUsers(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)

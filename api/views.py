from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.



@api_view(["POST"])
def createUserView(request):
    serializer=UserSerializer(data=request.data)
    if serializer.is_valid():
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
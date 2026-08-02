from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
# Create your views here.



@api_view(["POST"])
def createUserView(request):
    serializer=UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def Users_list(request):
     user=User.objects.all()
     serializer=UserSerializer(user,many=True)
     return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(["PUT"])
def Users_list(request,pk):
     user=User.objects.get(pk=pk)
     serializer=UserSerializer(user,data=request.data,many=False)
     if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
     return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)



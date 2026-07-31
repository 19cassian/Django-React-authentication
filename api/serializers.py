from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
      class Meta:
            model= User
            fields=["username","email","password"]


          #overriding the save method for the user
      def createUser(self,validated_data):
            username=validated_data["username"]
            email=validated_data["email"]
            password=validated_data["password"]
            user=User.objects.create_user(username=username,email=email,password=password)
            user.save();


              

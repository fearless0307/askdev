from django.shortcuts import render
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import request
from users.models import Profile, FavouriteQuestion
from users.serializers import ProfileSerializer, FavouriteQuestionSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class User_class(APIView):
    
    def get(self, request, format=None):
        user_profile = Profile.objects.all()
        serializer = ProfileSerializer(user_profile, context={'request': request}, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class User_Detail_class(APIView):
   
    def get_object(self, pk):
        try:
            return Profile.objects.get(id=pk)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user_profile = self.get_object(pk)
        serializer = ProfileSerializer(user_profile)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user_profile = self.get_object(pk)
        serializer = ProfileSerializer(user_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user_profile = self.get_object(pk)
        user_profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
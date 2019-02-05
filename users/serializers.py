from rest_framework import serializers
from users.models import Profile, FavouriteQuestion
from rest_framework import request
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Profile
        fields = ('profession', 'phone', 'profile_image', 'cover_image')


class FavouriteQuestionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = FavouriteQuestion

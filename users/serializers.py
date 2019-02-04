from rest_framework import serializers
from .models  import Profile ,FavouriteQuestion
from rest_framework import request



class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        # extra_fields = ['pizzas']


class FavouriteQuestionSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(many=False,
                                            read_only=True,
                                            view_name='user-detail',
                                            lookup_url_kwarg='pk')
    class Meta:
        model = FavouriteQuestion
        fields = '__all__'
        extra_fields = ['user']
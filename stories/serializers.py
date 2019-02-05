from rest_framework import serializers
from stories.models import Story, StoryTag, StoryReaction

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ('author', 'story', 'created_at','modified_at')

class StoryTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryTag
        fields = ('story', 'tag')

class StoryReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryReaction
        fields = ('author', 'story', 'reaction')


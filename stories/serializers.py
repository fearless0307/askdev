from rest_framework import serializers
from stories.models import Story, StoryTag, StoryReaction
from users.serializers import UserSerializer


class StoryTagSerializer(serializers.HyperlinkedModelSerializer):
    tag_name = serializers.ReadOnlyField(source='tag.name', read_only=True)

    class Meta:
        model = StoryTag
        fields = ('story', 'tag', 'tag_name')


class StoryReactionSerializer(serializers.HyperlinkedModelSerializer):
    reaction_name = serializers.ReadOnlyField(source='reaction.name', read_only=True)

    class Meta:
        model = StoryReaction
        fields = ('story', 'author', 'reaction', 'reaction_name')


class StorySerializer(serializers.HyperlinkedModelSerializer):
    tags = StoryTagSerializer(source='storytag_set', many=True)
    reactions = StoryReactionSerializer(source='storyreaction_set', many=True)

    class Meta:
        many = True
        model = Story
        # fields = ('author', 'story', 'created_at','modified_at')
        fields = ('url', 'id', 'author', 'title', 'story', 'tags', 'reactions', 'created_at', 'modified_at')

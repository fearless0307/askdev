from rest_framework import serializers
from stories.models import Story, StoryTag, StoryReaction
from users.serializers import UserSerializer


class StoryTagSerializer(serializers.HyperlinkedModelSerializer):
    tag_name = serializers.ReadOnlyField(source='tag.name', read_only=True)

    class Meta:
        model = StoryTag
        fields = ('story', 'tag', 'tag_name')
        extra_kwargs = {
            'tag': {'lookup_field': 'name'}
        }


class StoryReactionSerializer(serializers.HyperlinkedModelSerializer):
    author_name = serializers.ReadOnlyField(
        source='author.username', read_only=True)
    reaction_name = serializers.ReadOnlyField(
        source='reaction.name', read_only=True)
    reaction_score = serializers.ReadOnlyField(
        source='reaction.score', read_only=True)

    class Meta:
        model = StoryReaction
        fields = ('story', 'author', 'reaction', 'author_name',
                  'reaction_name', 'reaction_score')


class StorySerializer(serializers.HyperlinkedModelSerializer):
    tags = StoryTagSerializer(source='storytag_set', many=True)
    reactions = StoryReactionSerializer(source='storyreaction_set', many=True)

    class Meta:
        many = True
        model = Story
        fields = ('url', 'id', 'author', 'title', 'story', 'tags',
                  'reactions', 'created_at', 'modified_at')

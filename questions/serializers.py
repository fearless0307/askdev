from rest_framework import serializers
from questions.models import Reply, QuestionReaction, Tag

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ('author', 'answer', 'reply')

class QuestionReactionSerializer(serializers.ModelSerializer):
    # match = serializers.HyperlinkedRelatedField( many=False, view_name='match-detail', lookup_url_kwarg = 'pk', read_only=True)
    class Meta:
        model = QuestionReaction
        fields = ('question','reaction','author')


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)
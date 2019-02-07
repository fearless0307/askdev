from questions.models import Question, Answer, Reaction
from rest_framework import request, serializers
from questions.models import Reply, QuestionReaction, Tag, QuestionTag
from rest_framework.reverse import reverse
from stories.models import StoryTag
from askdev.utils import ParameterisedHyperlinkedIdentityField
                       

class ReplySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Reply
        fields = ('url', 'author', 'reply')


class QuestionReactionSerializer(serializers.HyperlinkedModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username', read_only=True)
    # author_id = serializers.ReadOnlyField(source='author.id', read_only=True)
    reaction_name = serializers.ReadOnlyField(source='reaction.name', read_only=True)
    reaction_score = serializers.ReadOnlyField(source='reaction.score', read_only=True)
    class Meta:
        model = QuestionReaction
        fields = ('question', 'reaction', 'author','author','author_name','reaction_name','reaction_score')


class TagSerializer(serializers.HyperlinkedModelSerializer):
    # questions = serializers.HyperlinkedRelatedField(view_name='tags-question-detail', read_only=True)
    questions = serializers.HyperlinkedIdentityField(view_name='tag-question-detail', lookup_field='name', read_only=True)
    stories = serializers.HyperlinkedIdentityField(view_name='tag-story-detail', lookup_field='name', read_only=True)
    
    class Meta:
        model = Tag
        fields = ('url', 'name','questions', 'stories')
        lookup_field = 'name'
        extra_kwargs = {
            'url': {'lookup_field': 'name'}
        }


class ReactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reaction
        fields = ('url', 'name', 'score', )


class QuestionTagSerializer(serializers.HyperlinkedModelSerializer):
    tag_name = serializers.ReadOnlyField(source='tag.name', read_only=True)

    class Meta:
        model = QuestionTag
        fields = ('question','tag', 'tag_name')
        extra_kwargs = {
            'tag': {'lookup_field': 'name'}
        }


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    answers = serializers.HyperlinkedIdentityField(view_name='question-answers')
    # author_name = serializers.ReadOnlyField(source='author.username', read_only=True)
    # author_id = serializers.ReadOnlyField(source='author.id', read_only=True)
    tags = QuestionTagSerializer(source='questiontag_set', many=True)
    reactions = QuestionReactionSerializer(source='questionreaction_set', many=True)
    class Meta:
        many=True
        model = Question
        fields = ['url', 'id', 'author', 'question', 'description', 'created_at',
                  'modified_at', 'answers','reactions', 'tags']


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    url = ParameterisedHyperlinkedIdentityField(
            view_name="answer-detail",
            lookup_fields=(('question_id', 'qid'), ('id', 'pk')),
            read_only=True)

    replies = ReplySerializer(source='reply_set', many=True)
    class Meta:
        model = Answer
        fields = ('url', 'question', 'id', 'author', 'answer', 'is_satisfied',
                  'modified_at', 'created_at', 'replies' )

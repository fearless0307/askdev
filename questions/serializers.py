from questions.models import Question, Answer, Reaction
from rest_framework import request, serializers
from questions.models import Reply, QuestionReaction, Tag, QuestionTag
from rest_framework.reverse import reverse


class ParameterisedHyperlinkedIdentityField\
      (serializers.HyperlinkedIdentityField):

    lookup_fields = (('pk', 'pk'),)

    def __init__(self, *args, **kwargs):
        self.lookup_fields = kwargs.pop('lookup_fields', self.lookup_fields)
        super(ParameterisedHyperlinkedIdentityField, self)\
            .__init__(*args, **kwargs)

    def get_url(self, obj, view_name, request, format):
        kwargs = {}
        for model_field, url_param in self.lookup_fields:
            attr = obj
            for field in model_field.split('.'):
                attr = getattr(attr, field)
            kwargs[url_param] = attr

        return reverse(view_name, kwargs=kwargs, request=request,
                       format=format)
                       
#

class ReplySerializer(serializers.HyperlinkedModelSerializer):
    

    class Meta:
        model = Reply
        fields = ('url', 'author',   'reply')


class QuestionReactionSerializer(serializers.HyperlinkedModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username', read_only=True)
    # author_id = serializers.ReadOnlyField(source='author.id', read_only=True)
    reaction_name = serializers.ReadOnlyField(source='reaction.name', read_only=True)
    reaction_score = serializers.ReadOnlyField(source='reaction.score', read_only=True)
    class Meta:
        model = QuestionReaction
        fields = ('question', 'reaction', 'author','author','author_name','reaction_name','reaction_score')


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)





class ReactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reaction
        fields = ('url', 'name', 'score', )



class QuestionTagSerializer(serializers.HyperlinkedModelSerializer):
    # question_id = serializers.ReadOnlyField(source='question', read_only=True)
    tag_name = serializers.ReadOnlyField(source='tag.name', read_only=True)

    class Meta:
        model = QuestionTag
        fields = ('question','tag','tag_name' )


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    answers = serializers.HyperlinkedIdentityField(view_name='question-answers')
    author_name = serializers.ReadOnlyField(source='author.username', read_only=True)
    author_id = serializers.ReadOnlyField(source='author.id', read_only=True)
    tags = QuestionTagSerializer(source='questiontag_set', many=True)
    reactions = QuestionReactionSerializer(source='questionreaction_set', many=True)
    class Meta:
        many=True
        model = Question
        fields = ['url', 'id', 'author','author_name', 'author_id', 'question', 'created_at',
                  'modified_at', 'answers','reactions', 'tags']


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    url = ParameterisedHyperlinkedIdentityField(
            view_name="answer-detail",
            lookup_fields=(('question_id', 'qid'), ('id', 'pk')),
            read_only=True)

    
    # replies = serializers.HyperlinkedIdentityField(view_name='answer-reply')
    # author_name = serializers.ReadOnlyField(source='author.username', read_only=True)
    # author_id = serializers.ReadOnlyField(source='author.id', read_only=True)
    replies = ReplySerializer(source='reply_set', many=True)
    class Meta:
        model = Answer
        fields = ('url', 'question', 'id', 'author', 'answer', 'is_satisfied',
                  'modified_at', 'created_at', 'replies' )



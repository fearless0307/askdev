from questions.models import Question, Answer, Reaction
from rest_framework import request, serializers
from questions.models import Reply, QuestionReaction, Tag, QuestionTag
from rest_framework.reverse import reverse

class ParameterisedHyperlinkedIdentityField(serializers.HyperlinkedIdentityField):
    """
    Represents the instance, or a property on the instance, using hyperlinking.

    lookup_fields is a tuple of tuples of the form:
        ('model_field', 'url_parameter')
    """
    lookup_fields = (('pk', 'pk'),)

    def __init__(self, *args, **kwargs):
        self.lookup_fields = kwargs.pop('lookup_fields', self.lookup_fields)
        super(ParameterisedHyperlinkedIdentityField, self)\
            .__init__(*args, **kwargs)

    def get_url(self, obj, view_name, request, format):
        """
        Given an object, return the URL that hyperlinks to the object.

        May raise a `NoReverseMatch` if the `view_name` and `lookup_field`
        attributes are not configured to correctly match the URL conf.
        """
        kwargs = {}
        for model_field, url_param in self.lookup_fields:
            attr = obj
            for field in model_field.split('.'):
                attr = getattr(attr, field)
            kwargs[url_param] = attr

        return reverse(view_name, kwargs=kwargs, request=request,
                       format=format)

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    answers =  serializers.HyperlinkedIdentityField(view_name='question-answers')
    tags =  serializers.HyperlinkedIdentityField(view_name='question-tags')
    class Meta:
        model = Question
        fields = ['url', 'id', 'author', 'question', 'created_at', 'modified_at', 'answers', 'questionreaction_set', 'tags']


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    url = ParameterisedHyperlinkedIdentityField(
            view_name="answer-detail",
            lookup_fields=(('question_id', 'qid'), ('id', 'pk')),
            read_only=True)
    class Meta:
        model = Answer
        fields = ('url','question', 'id', 'author', 'answer', 'is_satisfied',
                  'modified_at', 'created_at','reply_set')


class ReplySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reply
        fields = ('author', 'answer', 'reply')


class QuestionReactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuestionReaction
        fields = ('question', 'reaction', 'author')


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)


class QuestionTagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuestionTag
        fields = '__all__'


class ReactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reaction
        fields = ('url','name', 'score', )

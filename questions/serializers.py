from rest_framework import serializers
from .models  import Question ,Answer
from rest_framework import request


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['id','author','question','created_at','modified_at']
       
        


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
   
    
    question = serializers.HyperlinkedRelatedField(many=False,
                                            read_only=True,
                                            view_name='question-detail',
                                            lookup_url_kwarg='pk')

    user = serializers.HyperlinkedRelatedField(many=False,
                                            read_only=True,
                                            view_name='user-detail',
                                            lookup_url_kwarg='pk')
    class Meta:
        model = Answer
        fields = ('question','id', 'author', 'answer','is_satisfied','modified_at', 'created_at')
       

from questions.models import Reply, QuestionReaction, Tag, QuestionTag, Answer

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ('author', 'answer', 'reply')

class QuestionReactionSerializer(serializers.ModelSerializer):
    # match = serializers.HyperlinkedRelatedField( many=False, view_name='match-detail', lookup_url_kwarg = 'pk', read_only=True)
    class Meta:
        model = QuestionReaction
        fields = ('question','reaction','author')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)

class QuestionTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionTag
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
from rest_framework import serializers
from .models  import Question ,Answer
from rest_framework import request


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
        # extra_fields = ['pizzas']
        


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
        # fields = '__all__'
        # extra_fields = ['question']

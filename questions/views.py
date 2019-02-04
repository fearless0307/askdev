from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import request
from questions.models import Question, Answer
from questions.serializers import QuestionSerializer, AnswerSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from questions.models import Reply, QuestionReaction, Tag, QuestionTag, Answer
from questions.serializers import ReplySerializer, QuestionReactionSerializer, TagSerializer, QuestionTagSerializer, AnswerSerializer

def home(request):
    return render(request, 'questions/index.html', )


class Question_class(APIView):
    
    def get(self, request, format=None):
        question = Question.objects.all()
        serializer = QuestionSerializer(question, context={'request': request}, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = QuestionSerializer(data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Question_Detail_class(APIView):
   
    def get_object(self, pk):
        try:
            return Question.objects.get(id=pk)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = QuestionSerializer(question, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = QuestionSerializer(question, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        question = self.get_object(pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class Reply_list(APIView):
    def get(self, request, format=None):
        reply = Reply.objects.all()
        serializer = ReplySerializer(reply, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Reply_detail(APIView):
    def get_object(self, pk):
        try:
            return Reply.objects.get(pk=pk)
        except Reply.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        reply = Reply.objects.get(pk=pk)
        serializer = ReplySerializer(reply)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        reply = Reply.objects.get(pk=pk)
        serializer = ReplySerializer(reply, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    def delete(self, request, pk, format=None):
        reply = Reply.objects.get(pk=pk)
        reply.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class QuestionReaction_list(APIView):
    def get(self, request, format=None):
        reaction = QuestionReaction.objects.all()
        serializer = QuestionReactionSerializer(reaction, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = QuestionReaction(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuestionReaction_detail(APIView):
    def get_object(self, pk):
        try:
            return QuestionReaction.objects.get(pk=pk)
        except QuestionReaction.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        reaction = QuestionReaction.objects.get(pk=pk)
        serializer = QuestionReactionSerializer(reaction)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        reaction = QuestionReaction.objects.get(pk=pk)
        serializer = QuestionReaction(reaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    def delete(self, request, pk, format=None):
        reaction = QuestionReaction.objects.get(pk=pk)
        reaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Tags_list(APIView):
    def get(self, request, format=None):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Tags_detail(APIView):
    def get_object(self, pk):
        try:
            return Tag.objects.get(pk=pk)
        except Tag.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        tags = Tag.objects.get(pk=pk)
        serializer = TagSerializer(tags)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        tags = Tag.objects.get(pk=pk)
        serializer = TagSerializer(tags, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    def delete(self, request, pk, format=None):
        tags = Tag.objects.get(pk=pk)
        tags.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class QuestionTag_list(APIView):
    def get(self, request, format=None):
        question_tag = QuestionTag.objects.all()
        serializer = QuestionTagSerializer(question_tag, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = QuestionTagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuestionTag_detail(APIView):
    def get_object(self, pk):
        try:
            return QuestionTag.objects.get(pk=pk)
        except QuestionTag.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        question_tag = QuestionTag.objects.get(pk=pk)
        serializer = QuestionTagSerializer(question_tag)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        question_tag = QuestionTag.objects.get(pk=pk)
        serializer = QuestionTagSerializer(question_tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    def delete(self, request, pk, format=None):
        question_tag = QuestionTag.objects.get(pk=pk)
        question_tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Answer_list(APIView):
    def get(self, request, format=None):
        answer = Answer.objects.all()
        serializer = AnswerSerializer(answer, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Answer_detail(APIView):
    def get_object(self, pk):
        try:
            return Answer.objects.get(pk=pk)
        except Answer.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        answer = Answer.objects.get(pk=pk)
        serializer = AnswerSerializer(answer)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        answer = Answer.objects.get(pk=pk)
        serializer = AnswerSerializer(answer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    def delete(self, request, pk, format=None):
        answer = Answer.objects.get(pk=pk)
        answer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

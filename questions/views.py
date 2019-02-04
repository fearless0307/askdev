from django.shortcuts import render

# Create your views here.
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from questions.models import Reply, QuestionReaction, Tag
from questions.serializers import ReplySerializer, QuestionReactionSerializer, TagsSerializer

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
        serializer = TagsSerializer(tags, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TagsSerializer(data=request.data)
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
        serializer = TagsSerializer(tags)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        tags = Tag.objects.get(pk=pk)
        serializer = TagsSerializer(tags, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    def delete(self, request, pk, format=None):
        tags = Tag.objects.get(pk=pk)
        tags.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

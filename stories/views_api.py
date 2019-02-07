from django.shortcuts import render
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from stories.models import Story, StoryReaction, StoryTag
from stories.serializers import StorySerializer, StoryReactionSerializer,\
    StoryTagSerializer


class Story_list(APIView):
    def get(self, request, format=None):
        story = Story.objects.all()
        serializer = StorySerializer(story, many=True,
                                     context={'request': request})
        return Response(serializer.data)


class Story_detail(APIView):
    def get_object(self, pk):
        try:
            return Story.objects.get(pk=pk)
        except Story.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        story = Story.objects.get(pk=pk)
        serializer = StorySerializer(story, context={'request': request})
        return Response(serializer.data)


class Tags_stories(APIView):
    def get(self, request, name, format=None):
        story_tag = StoryTag.objects.filter(tag__name=name).all()
        serializer = StoryTagSerializer(story_tag, context={'request': request},
                               many=True)
        return Response(serializer.data)


# class StoryTag_list(APIView):
#     def get(self, request, format=None):
#         story_tag = StoryTag.objects.all()
#         serializer = StoryTagSerializer(story_tag, many=True, context={'request': request})
#         return Response(serializer.data)


# class StoryTag_detail(APIView):
#     def get_object(self, pk):
#         try:
#             return StoryTag.objects.get(pk=pk)
#         except StoryTag.DoesNotExist:
#             return Http404

#     def get(self, request, pk, format=None):
#         story_tag = StoryTag.objects.get(pk=pk)
#         serializer = StoryTagSerializer(story_tag, context={'request': request})
#         return Response(serializer.data)


# class StoryReaction_list(APIView):
#     def get(self, request, pk1, format=None):
#         # diaplay all reaction of a story
#         story_reaction = StoryReaction.objects.filter(story__id=pk1).all()
#         serializer = StoryReactionSerializer(story_reaction, many=True, context={'request': request})
#         return Response(serializer.data)


# class StoryReaction_detail(APIView):
#     def get_object(self, pk1, pk2):
#         try:
#             return StoryReaction.objects.filter(id=pk2)
#         except StoryReaction.DoesNotExist:
#             return Http404

#     def get(self, request, pk1, pk2, format=None):
#         story_reaction = StoryReaction.objects.filter(id=pk2)
#         print(story_reaction)
#         serializer = StoryReactionSerializer(story_reaction, many=True, context={'request': request})
#         return Response(serializer.data)

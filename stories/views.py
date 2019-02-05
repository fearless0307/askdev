from django.shortcuts import render
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from . models import Story
# Create your views here.
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from stories.models import Story, StoryReaction, StoryTag
from stories.serializers import StorySerializer, StoryReactionSerializer, StoryTagSerializer

class Story_list(APIView):
    def get(self, request, format=None):
        story = Story.objects.all()
        serializer = StorySerializer(story, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Story_detail(APIView):
    def get_object(self, pk):
        try:
            return Story.objects.get(pk=pk)
        except Story.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        story = Story.objects.get(pk=pk)
        serializer = StorySerializer(story)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        story = Story.objects.get(pk=pk)
        serializer = StorySerializer(story, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    def delete(self, request, pk, format=None):
        story = Story.objects.get(pk=pk)
        story.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StoryTag_list(APIView):
    def get(self, request, format=None):
        story_tag = StoryTag.objects.all()
        serializer = StoryTagSerializer(story_tag, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StoryTag_detail(APIView):
    def get_object(self, pk):
        try:
            return StoryTag.objects.get(pk=pk)
        except StoryTag.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        story_tag = StoryTag.objects.get(pk=pk)
        serializer = StoryTagSerializer(story_tag)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        story_tag = StoryTag.objects.get(pk=pk)
        serializer = StoryTagSerializer(story_tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    def delete(self, request, pk, format=None):
        story_tag = StoryTag.objects.get(pk=pk)
        story_tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StoryReaction_list(APIView):
    def get(self, request, format=None):
        story_reaction = StoryReaction.objects.all()
        serializer = StoryReactionSerializer(story_reaction, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StoryReactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StoryReaction_detail(APIView):
    def get_object(self, pk):
        try:
            return StoryReaction.objects.get(pk=pk)
        except StoryReaction.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        story_reaction = StoryReaction.objects.get(pk=pk)
        serializer = StoryReactionSerializer(story_reaction)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        story_reaction = StoryReaction.objects.get(pk=pk)
        serializer = StoryReactionSerializer(story_reaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    def delete(self, request, pk, format=None):
        story_reaction = StoryReaction.objects.get(pk=pk)
        story_reaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def stories_home(request):
    '''
    Home page for stories app.
    Returns to the home page of the stories app.
    '''
    context = {
        'stories': Story.objects.all()
    }
    return render(request, 'stories/home.html', context)

class StorylistView(ListView):
    model = Story
    template_name = 'questions/home.html'
    context_object_name = 'stories'
    ordering = ['-created_at']

class StorydetailView(DetailView):
    model = Story

class StorycreateView(LoginRequiredMixin, CreateView):
    model = Story
    fields = ['title', 'story']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class StoryupdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Story
    fields = ['title', 'story']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        story = self.get_object()
        if self.request.user == story.author:
            return True
        return False

class StorydeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Story
    success_url = '/stories/'

    def test_func(self):
        story = self.get_object()
        if self.request.user == story.author:
            return True
        return False
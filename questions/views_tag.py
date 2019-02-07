from django.shortcuts import render
from questions.models import Tag, QuestionTag, Answer
import wikipedia
import requests
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import JsonResponse


def tag_home(request):
    tags_url = request.build_absolute_uri(reverse('tag'))
    context = {
        'title': 'Tags',
        'tags_url': tags_url
    }
    return render(request, 'questions/tag.html', context)


def tag_question(request, name):
    view_type = request.GET.get('view', 'card')
    tag_questions = request.build_absolute_uri(reverse('tag-question-detail', kwargs={'name': name}))
    print(tag_questions)
    context = {
        'title': name,
        'tag_questions_url': tag_questions,
        'view_type': view_type,
    }
    return render(request, 'questions/tag_questions.html', context )


def tag_story(request, name):
    view_type = request.GET.get('view', 'card')
    tag_storys = request.build_absolute_uri(reverse('tag-story-detail', kwargs={'name': name}))
    print(tag_storys)
    context = {
        'title': name,
        'tag_stories_url': tag_storys,
        'view_type': view_type,
    }
    return render(request, 'questions/tag_stories.html', context )

def testing(request):
     return render(request, 'questions/testing.html')
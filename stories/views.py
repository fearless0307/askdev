from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from stories.models import Story, StoryTag, StoryReaction
from stories.forms import StoryForm, StoryTagForm, StoryReactionForm
from django.urls import reverse
import requests
from questions.models import Tag
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required


def stories_home(request):
    view_type = request.GET.get('view', 'card')
    print(view_type)
    stories_url = request.build_absolute_uri(reverse('story-list'))
    context = {
        'title': 'Stories',
        'stories_url': stories_url,
        'view_type': view_type,
    }
    return render(request, 'stories/stories.html', context)


def stories_detail(request, pk):
    story = Story.objects.get(id=pk)
    story_url = request.build_absolute_uri(reverse('story-detail', kwargs={'pk': pk}))
    context = {
        'title': 'Story',
        'story_url': story_url,
        'story': story,
    }
    return render(request, 'stories/story_detail.html', context)


@login_required
def stories_create(request):
    if request.method == 'POST':
        story_form = StoryForm(request.POST)
        storytag_form = StoryTagForm(request.POST)
        if story_form.is_valid() and storytag_form.is_valid():
            story_post = story_form.save(commit=False)
            storytag_post = storytag_form.save(commit=False)
            story_post.author = request.user
            story_post.created_at = timezone.now()
            story_post.save()
            storytag_post.story_id = story_post.id
            storytag_post.save()
            return redirect('stories-home')
    else:
        story_form = StoryForm()
        storytag_form = StoryTagForm()
        context = {
            'story_form': story_form,
            'storytag_form': storytag_form
        }
    return render(request, 'stories/story_create.html', context)#{'story_form': story_form})


@login_required
def stories_edit(request, pk):
    story = get_object_or_404(Story, pk=pk)
    if request.method == "POST":
        story_form = StoryForm(request.POST, instance=story)
        if story_form.is_valid():
            story_post = story_form.save(commit=False)
            story_post.author = request.user
            story_post.created_at = timezone.now()
            story_post.save()
            return redirect('stories-detail', pk=story_post.pk)
    else:
        story_form = StoryForm(instance=story)
    return render(request, 'stories/story_edit.html', {'story_form':story_form})


@login_required
def stories_delete(request, pk):
    story = Story.objects.get(pk=pk).delete()
    return redirect('stories-home')


# @login_required
def submit_like_reaction(request, pk):
    # liked = 1
    current_user = request.user
    story = Story.objects.filter(id=pk)
    # story_reaction = StoryReaction.objects.filter(author=current_user.id)
    context = {
        'liked': 1,
        'user': current_user,
        'story': story
    }
    return render(request, 'stories/test.html', context)


# @login_required
def submit_dislike_reaction(request):
    disliked = -1
    return HttpResponse(disliked)


# @login_required
def submit_clap_reaction(request):
    clapped = 2
    return HttpResponse(clapped)
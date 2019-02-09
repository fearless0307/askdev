from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from stories.models import Story, StoryTag, StoryReaction
from stories.forms import StoryForm, StoryReactionForm
from django.urls import reverse
import requests
from questions.models import Tag, Reaction
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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
    story_url = request.build_absolute_uri(
        reverse('story-detail', kwargs={'pk': pk}))
    story = Story.objects.get(id=pk)
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
        # storytag_form = StoryTagForm(request.POST)
        if story_form.is_valid():
            story_post = story_form.save(commit=False)
            story_post.author = request.user
            story_post.save()
            tag_ids = request.POST.get('tags').split(',')
            print(tag_ids)
            for tag_id in tag_ids:
                story_tag = StoryTag(tag_id=tag_id, story_id=story_post.id)
                story_tag.save()
            messages.success(
                request, f'Your story has been added!', extra_tags='success')
            return redirect('stories-home')
        else:
            messages.error(request, f'Something went wrong!',
                           extra_tags='danger')
    else:
        story_form = StoryForm()
        context = {
            'story_form': story_form,
        }
    return render(request, 'stories/story_create.html', context)


@login_required
def stories_edit(request, pk):
    story = get_object_or_404(Story, pk=pk)
    if request.method == "POST":
        story_form = StoryForm(request.POST, instance=story)
        if story_form.is_valid():
            story_post = story_form.save()
            # story_post.author = request.user
            # story_post.save()
            messages.success(
                request, f'Your story has been updated!', extra_tags='success')
            return redirect('stories-detail', pk=story_post.pk)
        else:
            messages.error(request, f'Something went wrong!',
                           extra_tags='danger')
    else:
        story_form = StoryForm(instance=story)
    return render(request, 'stories/story_edit.html',
                  {'story_form': story_form})


@login_required
def stories_delete(request, pk):
    story = Story.objects.get(pk=pk).delete()
    messages.success(
                request, f'Your story has been deleted successfully!', extra_tags='success')
    return redirect('user-profile')


@login_required
def submit_reaction(request, pk, name):
    current_user = request.user
    story = Story.objects.get(id=pk)
    name = '&#x'+name
    reaction = Reaction.objects.filter(name=name).first()
    story_reactions = StoryReaction.objects.filter(story=story, author=current_user).first()
    if story_reactions is not None:
        messages.error(request, f'You already gives reaction on this story!',
                           extra_tags='danger')
    else:
        story_reactions = StoryReaction(story=story, reaction=reaction, author=current_user)
        story_reactions.save()
        messages.success(
                request, f'Your reaction has been added!', extra_tags='success')
    return redirect('stories-detail', pk=pk)

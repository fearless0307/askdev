from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from stories.models import Story, StoryTag
from stories.forms import StoryForm, StoryTagForm
from questions.models import Tag
from django.http import HttpResponse

def stories_home(request):
    context = {
        'stories': Story.objects.all().order_by('-created_at'),
        'tags': StoryTag.objects.all()
    }
    return render(request, 'stories/home.html', context)


def stories_detail(request, pk):
    context = {
        'story' : get_object_or_404(Story, pk=pk),
        'tags' : get_object_or_404(StoryTag, story_id=pk)
    }
    return render(request, 'stories/story_detail.html', context)

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

def stories_delete(request, pk):
    story = Story.objects.get(pk=pk).delete()
    return redirect('stories-home')
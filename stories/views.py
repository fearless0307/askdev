from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from stories.models import Story


def stories_home(request):
    context = {
        'stories': Story.objects.all()
    }
    return render(request, 'stories/home.html', context)


class StorylistView(ListView):
    model = Story
    template_name = 'questions/home.html'
    context_object_name = 'stories'


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

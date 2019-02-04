from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Story
# Create your views here.

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
    template_name = 'stories/home.html'
    context_object_name = 'stories'
    ordering = ['-created_at']

class StorydetailView(DetailView):
    model = Story
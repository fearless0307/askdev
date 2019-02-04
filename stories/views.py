from django.shortcuts import render
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
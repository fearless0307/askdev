from django import forms
from stories.models import Story, StoryTag, StoryReaction
from questions.models import Tag

class StoryForm(forms.ModelForm):

    class Meta:
        model = Story
        fields = ('title', 'story',)

class StoryTagForm(forms.ModelForm):

    class Meta:
        model = StoryTag
        fields = ('tag',)
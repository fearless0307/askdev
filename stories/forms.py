from django import forms
from stories.models import Story, StoryTag, StoryReaction
from questions.models import Tag


class StoryForm(forms.ModelForm):

    class Meta:
        model = Story
        fields = ('title', 'story',)


class StoryReactionForm(forms.ModelForm):

    class Meta:
        model = StoryReaction
        fields = '__all__'

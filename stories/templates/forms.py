from django import forms
from stories.models import Story, StoryTag, StoryReaction

class StoryForm(forms.ModelForm):

    class Meta:
        pass

class StoryTagForm(forms.ModelForm):

    class Meta:
        pass
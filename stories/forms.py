from django import forms
from stories.models import Story, StoryTag, StoryReaction
from questions.models import Tag

class StoryForm(forms.ModelForm):

    class Meta:
        model = Story
        fields = ('title', 'story',)

# class StoryTagForm(forms.Form):

#     OPTIONS = Tag.objects.values_list('id', 'name')
#     print(OPTIONS)

#     OPTIONS_ = tuple([option for option in OPTIONS])
#     print(OPTIONS_)

#     tags = forms.MultipleChoiceField(widget=forms.SelectMultiple(attrs={'class': "form-control"}),
#                                              choices=OPTIONS_, )

#     # class Meta:
#     #     model = StoryTag
#     #     fields = ('tag',)

class StoryReactionForm(forms.ModelForm):

    class Meta:
        model = StoryReaction
        fields = '__all__'
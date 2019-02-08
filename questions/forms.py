from django import forms
from questions.models import Question, QuestionTag, QuestionReaction, Tag, Answer



class QuestionForm(forms.ModelForm):

    question = forms.CharField(widget=forms.Textarea(attrs={'rows':'2', 'required':''}))

    class Meta:
        model = Question
        fields = ('question', 'description')


class QuestionReactionForm(forms.ModelForm):

    class Meta:
        model = QuestionReaction
        fields = '__all__'


from django import forms
from questions.models import Question, QuestionTag, QuestionReaction, Tag, Answer



class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('question', 'description',)

class QuestionTagForm(forms.ModelForm):

    class Meta:
        model = QuestionTag
        fields = ('tag',)

class QuestionReactionForm(forms.ModelForm):

    class Meta:
        model = QuestionReaction
        fields = '__all__'


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ('answer',)
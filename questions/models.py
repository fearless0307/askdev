from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Tag(models.Model):
    name = models.CharField(max_length=75)

    def __str__(self):
        return f'Tag {self.name}'


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField()
    description = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'User {self.author.id} : Question {self.question}'


class QuestionTag(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f'Question {self.question.id} : Tag {self.tag.id}'


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()
    is_satisfied = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'User {self.author.id} Question {self.question.id}'\
                ' Answer {self.answer}'


class Reply(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'User {self.author.id} Answer {self.answer.id}'\
                ' Reply {self.reply}'

    


class Reaction(models.Model):
    name = models.CharField(max_length=75)
    score = models.IntegerField()

    def __str__(self):
        return f'Reaction {self.name} : Score {self.score}'


class QuestionReaction(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    reaction = models.ForeignKey(Reaction, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'User {self.author.id} : Question {self.question.id}' +\
               ' : Reaction {self.reaction.id}'

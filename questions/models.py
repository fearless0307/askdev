from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=75)

    def __str__(self):
        return f'Tag {self.name}'


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'User {self.author.id} : Question {self.question}'


class QuestionTags(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        db_table = "question_tags"

    def __str__(self):
        return f'Question {self.question.id} : Tag {self.tag.id}'


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()
    is_satisfied = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'User {self.author.id} Question {self.question.id}'\
                ' Answer {self.answer}'


class Reply(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    reply = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "replies"

    def __str__(self):
        return f'User {self.author.id} Answer {self.answer.id}'\
                ' Reply {self.reply}'


class Reaction(models.Model):
    name = models.CharField(max_length=75)
    score = models.IntegerField()

    def __str__(self):
        return f'Reaction {self.name} : Score {self.score}'


class QuestionReactions(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    reaction = models.ForeignKey(Reaction, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "question_reactions"

    def __str__(self):
        return f'User {self.author.id} : Question {self.question.id}'\
                ': Reaction {self.reaction.id}'

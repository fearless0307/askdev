from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from questions.models import Reaction, Tag


# Create your models here.
class Story(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    story = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'User {self.author.id} : Story {self.story}'


class StoryTag(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f'Story {self.story.id} : Tag {self.tag.id}'


class StoryReaction(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    reaction = models.ForeignKey(Reaction, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'User {self.author.id} : Story {self.story.id}'\
                ' : Reaction {self.reaction.id}'

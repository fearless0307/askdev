from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from questions.models import Reaction, Tag


# Create your models here.
class Story(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    story = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'User {self.author.id} : Story {self.story}'


class StoryTags(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        db_table = "story_tags"

    def __str__(self):
        return f'Story {self.story.id} : Tag {self.tag.id}'


class StoryReactions(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    reaction = models.ForeignKey(Reaction, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "story_reactions"

    def __str__(self):
        return f'User {self.author.id} : Story {self.story.id}'\
                ' : Reaction {self.reaction.id}'

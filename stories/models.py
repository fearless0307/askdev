from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from questions.models import Reaction, Tag
from ckeditor.fields import RichTextField
from django.urls import reverse


# Create your models here.
class Story(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True)
    story = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Author : {self.author} ID : {self.author.id} Title : {self.title} id-{self.id}'

    def get_absolute_url(self):
        return reverse('stories-detail', kwargs={'pk': self.pk})


class StoryTag(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'Story : {self.story.id} author: {self.story.author} Tag : {self.tag.name}'


class StoryReaction(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    reaction = models.ForeignKey(Reaction, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'User {self.author.id} : Story {self.story.id}'\
                ' : Reaction {self.reaction.id}'

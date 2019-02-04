from django.contrib import admin
from stories.models import Story, StoryReaction, StoryTag


# Register your models here.
admin.site.register(StoryTag)
admin.site.register(StoryReaction)
admin.site.register(Story)

from django.contrib import admin
from stories.models import Story, StoryReactions, StoryTags


# Register your models here.
admin.site.register(StoryTags)
admin.site.register(StoryReactions)
admin.site.register(Story)

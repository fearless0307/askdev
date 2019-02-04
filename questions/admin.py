from django.contrib import admin
from questions.models import Tag, Question, QuestionTag, Answer, Reply,\
    Reaction, QuestionReaction


# Register your models here.
admin.site.register(Tag)
admin.site.register(Question)
admin.site.register(QuestionTag)
admin.site.register(Answer)
admin.site.register(Reply)
admin.site.register(Reaction)
admin.site.register(QuestionReaction)

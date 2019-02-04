from django.contrib import admin
from questions.models import Tag, Question, QuestionTags, Answer, Reply,\
    Reaction, QuestionReactions



admin.site.register(Tag)
admin.site.register(Question)
admin.site.register(QuestionTags)
admin.site.register(Answer)
admin.site.register(Reply)
admin.site.register(Reaction)
admin.site.register(QuestionReactions)

from django.shortcuts import render
from questions.models import Tag, QuestionTag
import wikipedia


def tag_home(request):
    context = {
        'tags': Tag.objects.all()
    }
    return render(request, 'questions/tag.html', context)

def tag_detail(request, pk):
    tag= Tag.objects.filter(pk=pk).first()

    context = {
        'questions': QuestionTag.objects.filter(tag=pk),
        'tag': tag.name,
        'detail': wikipedia.summary(tag.name, sentences=3)
    }
    return render(request, 'questions/tag_detail.html', context)

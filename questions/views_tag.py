from django.shortcuts import render
from questions.models import Tag, QuestionTag, Answer
import wikipedia
import requests


def tag_home(request):
    context = {
        'tags': Tag.objects.all()
    }
    return render(request, 'questions/tag.html', context)

def tag_detail(request, pk):
    tag= Tag.objects.filter(name=pk).first()

    # response = requests.get('http://127.0.0.1:8000/api/questions/'+ str(pk)+'/')
    # api_data = response.json()
    # print(api_data)

    context = {
        'questions': QuestionTag.objects.filter(tag=tag.id),
        'tag': tag.name,
        # 'detail': wikipedia.summary(tag.name + 'Programming', sentences=3)
    }
    return render(request, 'questions/tag_detail.html', context)

def tag_answer(request, pk):
    answers = Answer.objects.filter(question=pk)
    print(answers)
    context = { 'answers': answers } 
    return render(request, 'questions/tag_answer.html', context )

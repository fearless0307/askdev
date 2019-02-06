from django.shortcuts import render
from django.contrib.auth.models import User
import requests
from datetime import datetime
from questions.models import Question


def questions_home(request):
    url = 'http://127.0.0.1:8000/api/questions/'
    response = requests.get(url)
    api_data = response.json()
    return render(request, 'questions/home.html', {'questions': api_data,'url':questions_url})


def question_detail(request,pk):
    url ='http://127.0.0.1:8000/api/questions/'+str(pk)+'/'
    print("pk=",pk,url)
    response = requests.get(url)
    api_data = response.json()
    answer_response = requests.get(api_data['answers'])
    api_answer_data = answer_response.json()
    return render(request, 'questions/question_detail.html', {'question_object': api_data, 'answer_object':api_answer_data})


def question_create(request):
    print("form",request)
    if request.method == 'POST': 
        form = request.POST 
        print("form=",form,request.user.id)
        user  = User.objects.get(id=request.user.id)
        question = Question(author=user,question=form['question'])
        question.save()
    return render(request, 'questions/question_create.html')


def question_delete(request,pk):
    question = Question.objects.get(id=pk)
    question.delete()
    return render(request, 'questions/question_create.html')


def question_update(request,pk):
    if request.method == 'POST': 
        form = request.POST 
        print("form=",form,request.user.id)
        question = Question.objects.get(id=pk)
        if question is not None:
            question.question = form['question']
            question.save()
            return render(request, 'questions/home.html')
    return render(request, 'questions/question_create.html')

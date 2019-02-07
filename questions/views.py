from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import requests
from datetime import datetime
from questions.models import Question
from django.urls import reverse

def questions_home(request):
    # questions_url = 'http://127.0.0.1:8000/api/questions/'
    # response = requests.get(questions_url)
    api_data = ""#response.json()
    questions_url = request.build_absolute_uri(reverse('questions'))
    # print(questions_url)
    return render(request, 'questions/home.html', {'questions': api_data,'questions_url':questions_url})


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
        redirect('questions/home.html')
    return render(request, 'questions/question_create.html')


def question_delete(request,pk):
    question = Question.objects.get(id=pk)
    question.delete()
    return render(request, 'questions/question_create.html')


def question_update(request,pk):
    if request.method == 'POST': 
        form = request.POST 
        # print("form=",form,request.user.id)
        question = Question.objects.get(id=pk)
        # print("done=done",question)
        if question is not None:
            print("done")
            question.question = form['question']
            question.save()
            return redirect('questions-home')
    return render(request, 'questions/question_create.html')

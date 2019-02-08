from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import requests
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from questions.forms import QuestionForm, QuestionTagForm
from datetime import datetime
from questions.models import Question
from django.urls import reverse

def questions_home(request):
    view_type = request.GET.get('view', 'card')
    
    print("show view = ",view_type)
    questions_url = request.build_absolute_uri(reverse('questions'))
    context = {
        'view_type': view_type,
        'questions_url':questions_url,
        'title': 'Questions',
    }
    return render(request, 'questions/home.html', context)


def question_detail(request,pk):
    question = Question.objects.get(id=pk)
    question_url = request.build_absolute_uri(reverse('question-detail', kwargs={'pk': pk}))
    print("question=url ==",question_url)
    context = {
        'title': 'Question',
        'question_url': question_url,
        'question': question,
    }
    return render(request, 'questions/question_detail.html', context)

@login_required
def question_create(request):
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        questiontag_form = QuestionTagForm(request.POST)
        if question_form.is_valid() and questiontag_form.is_valid():
            question_post = question_form.save(commit=False)
            questiontag_post = questiontag_form.save(commit=False)
            question_post.author = request.user
            question_post.created_at = timezone.now()
            question_post.save()
            questiontag_post.question_id = question_post.id
            questiontag_post.save()
            return redirect('stories-home')
    else:
        question_form = QuestionForm()
        questiontag_form = QuestionTagForm()
        context = {
            'question_form': question_form,
            'questiontag_form': questiontag_form
        }
    return render(request, 'questions/question_create.html', context)


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

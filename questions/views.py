from django.shortcuts import render, redirect
import requests
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from questions.forms import QuestionForm
from questions.models import Question, QuestionTag
from django.urls import reverse


def questions_home(request):
    view_type = request.GET.get('view', 'card')

    print("show view = ", view_type)
    questions_url = request.build_absolute_uri(reverse('questions'))
    context = {
        'view_type': view_type,
        'questions_url': questions_url,
        'title': 'Questions',
    }
    return render(request, 'questions/home.html', context)


def questions_search(request):
    view_type = request.GET.get('view', 'card')
    search = request.GET.get('search', '')

    print("show view = ", view_type)
    questions_url = request.build_absolute_uri(reverse('questions') + '?search='+search)
    context = {
        'view_type': view_type,
        'questions_url': questions_url,
        'title': 'Questions',
    }
    return render(request, 'questions/home.html', context)


def question_detail(request, pk):
    question_url = request.build_absolute_uri(
        reverse('question-detail', kwargs={'pk': pk}))
    print("question=url ==", question_url)
    context = {
        'title': 'Question',
        'question_url': question_url,
    }
    return render(request, 'questions/question_detail.html', context)


@login_required
def question_create(request):
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            question_post = question_form.save(commit=False)
            question_post.author = request.user
            question_post.save()
            tag_ids = request.POST.get('tags').split(',')
            print(tag_ids)
            for tag_id in tag_ids:
                if tag_id == None:
                    tag_id = 8
                question_tag = QuestionTag(tag_id=tag_id, question_id=question_post.id)
                question_tag.save()
            messages.success(
                request, f'Your question has been added!', extra_tags='success')
            return redirect('questions-home')
        else:
            messages.error(request, f'Something went wrong!',
                           extra_tags='danger')
    else:
        question_form = QuestionForm()
        context = {
            'question_form': question_form,
        }
    return render(request, 'questions/question_create.html', context)


@login_required
def question_delete(request, pk):
    question = Question.objects.get(id=pk)
    question.delete()
    return render(request, 'questions/question_create.html')


@login_required
def question_update(request, pk):
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

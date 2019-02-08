from django.shortcuts import render, redirect
import requests
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from questions.forms import QuestionForm
from datetime import datetime
from questions.models import Question, Answer, Reply
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User


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

@login_required
def answer_create(request):
    
    if request.method == 'POST':
        try:
            print("inside")
            answer = request.POST.get('answer')
            qid = request.POST.get('question')
            question = Question.objects.get(id=qid)
            if request.user.id ==question.author_id:
                messages.success(request, f'You Can not answer your own question ',extra_tags='warning')
            else:
                user  = User.objects.get(id=request.user.id)
                answer =Answer(author=user,question=question,answer=answer)
                print("id=",answer)
                answer.save()
                messages.success(request, f'Answer Posted ',extra_tags='success')
                print("answer",answer)
                print("question",qid)
        except:
            # print
            messages.success(request, f'Some Thing Went Wrong',extra_tags='error')
       
    return redirect('questions-detail', pk=qid)

@login_required
def reply_create(request):
    
    if request.method == 'POST':
        # try:
        print("inside")
        reply = request.POST.get('reply')
        qid = request.POST.get('question')
        aid = request.POST.get('answer')
        answer = Answer.objects.get(id=aid)
        user  = User.objects.get(id=request.user.id)
        reply =Reply(author=user,answer=answer,reply=reply)
        print("id=",reply)
        reply.save()
        messages.success(request, f'Reply Posted ',extra_tags='success')
        print("answer",reply)
        print("question",aid)
        # except:
        #     # print
        #     messages.success(request, f'Some Thing Went Wrong',extra_tags='error')
       
    return redirect('questions-detail', pk=qid)
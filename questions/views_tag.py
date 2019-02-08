from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import requests
from questions.models import Tag, QuestionTag, Answer


def tag_home(request):
    tags_url = request.build_absolute_uri(reverse('tag'))
    context = {
        'title': 'Tags',
        'tags_url': tags_url
    }
    return render(request, 'questions/tag.html', context)


def tag_question(request, name):
    view_type = request.GET.get('view', 'card')
    tag_questions = request.build_absolute_uri(
        reverse('tag-question-detail', kwargs={'name': name}))
    print(tag_questions)
    context = {
        'title': name,
        'tag_questions_url': tag_questions,
        'view_type': view_type,
    }
    return render(request, 'questions/tag_questions.html', context)


def tag_story(request, name):
    view_type = request.GET.get('view', 'card')
    tag_storys = request.build_absolute_uri(
        reverse('tag-story-detail', kwargs={'name': name}))
    print(tag_storys)
    context = {
        'title': name,
        'tag_stories_url': tag_storys,
        'view_type': view_type,
    }
    return render(request, 'questions/tag_stories.html', context)


def testing(request):
    if request.method == 'POST':
        form = request.POST
        #print(form)
        main(form)
        return redirect('questions-home')
    return render(request, 'questions/testing.html')


# Send as many times you like
# Also can send to multiple people
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def main(form):
    #all_email = ['amrit.prasad@mountblue.io','jaiprakash.patidar@mountblue.io', 'bhola.kumar@mountblue.io', 'prajwal.chigod@mountblue.io']
    all_email = ['kramrit6@gmail.com']
    name = form['name']
    email = form['email']
    message = form['message']
    contact = form['contact']

    message = 'From '+ email + "<br>" + message
    
    for send_to_email in all_email:
        email = 'askdev.jpba@gmail.com'
        password = 'AskDev@12'

        subject = "AskDev"
        server = smtplib.SMTP(host='smtp.gmail.com', port=587)
        server.starttls()
        server.login(email, password)
        
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = send_to_email
        msg['Subject'] = subject

        part = MIMEText(message, 'html')
        msg.attach(part)
        server.send_message(msg)
        del msg 
        server.quit()
        # <QueryDict: {'csrfmiddlewaretoken': ['SoItB6okJXWmWnZqJaDRVM1KqjAZpNPxRIsj4hgWhy74H5RXglA6yhvsoInuXcsz'],
        #  'name': ['Python'], 'email': ['admin@log.com'], 'Message': ['my mesaeg'], 'contact': ['']}>
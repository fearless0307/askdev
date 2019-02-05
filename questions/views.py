from django.shortcuts import render


def questions_home(request):
    return render(request, 'questions/home.html', {'title': 'Home'})

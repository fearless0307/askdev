from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from stories.models import Story
from users.models import Profile, FavouriteQuestion
from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from questions.models import Question, Answer


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!' +
                                      'You are now able to login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,
                                   instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'title': 'Edit Profile',
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)

#It will show the user profile with all of his details
@login_required
def display_user_profile(request):
    user = request.user
    my_questions = Question.objects.filter(author=user)
    my_answers = Answer.objects.filter(author=user)
    my_stories = Story.objects.filter(author=user)
    my_fav_questions = FavouriteQuestion.objects.filter(author=user)
    content = {
        'my_questions': my_questions,
        'my_answers': my_answers,
        'my_stories': my_stories,
        'my_fav_questions':my_fav_questions
    }
    # pass
    return render(request, 'users/user_profile.html', content)


# It will show all the bookmarked questions of the user
@login_required
def fav_questions(request):
    # print(request.user)
    current_user = request.user
    fav = FavouriteQuestion.objects.filter(author=current_user)
    print(fav)
    # return render(request, 'users/fav_questions.html',{'questions': fav})
    # rendering to tag_detail
    return render(request, 'questions/tag_detail.html', {'questions': fav})


# It will show all the posts of an logined user
@login_required
def my_posts(request):
    current_user = request.user
    my_questions = Question.objects.filter(author=current_user)
    # print(my_questions)
    my_answers = Answer.objects.filter(author=current_user)
    # print(my_answers)
    my_stories = Story.objects.filter(author=current_user)
    content = {
        'my_questions': my_questions,
        'my_answers': my_answers,
        'my_stories': my_stories
    }
    return render(request, 'users/my_posts.html', content)

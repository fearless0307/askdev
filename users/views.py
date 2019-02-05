from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework import request, status
from users.models import Profile, FavouriteQuestion
from users.serializers import UserSerializer, FavouriteQuestionSerializer,\
    ProfileSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from questions.models import Question
from questions.serializers import QuestionSerializer

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


class User_class(APIView):

    def get(self, request, format=None):
        user = User.objects.all()
        serializer = UserSerializer(user, context={'request': request},
                                    many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class User_Detail_class(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(id=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        user_serializer = UserSerializer(user, context={'request': request})
        profile = Profile.objects.filter(id=pk).first()
        if profile is not None:
            profile_serializer =\
                ProfileSerializer(profile, context={'request': request})
            return \
                Response({**user_serializer.data, **profile_serializer.data})
        else:
            return Response(user_serializer.data)

    # def put(self, request, pk, format=None):
    #     user1 = self.get_object(pk)
    #     profile = Profile.objects.get(id=pk)
    #     print("data=",request.data,profile.user,user1.id,pk)
    #     user = request.data
    #     user_data = {
    #         'username':user['username'],
    #         'email': user['email'],
    #     }
    #     user_profile = {
    #         'user':pk,
    #         'profession':user['profession'],
    #         'phone': user['phone'],
    #         'profile_image': user['profile_image'],
    #         'cover_image': user['cover_image'],
    #     }
    #     print("profile",user1)
    #     user_serializer =\
    #       UserSerializer(user1, data=user_data,context={'request': request})
    #     user_profile_serializer =\
    #       ProfileSerializer(profile,
    #                         data=user_profile,context={'request': request})
    #     print("cond=",user_serializer.is_valid() ,
    #           user_profile_serializer.is_valid())
    #     if user_serializer.is_valid() and user_profile_serializer.is_valid():
    #         user_serializer.save()
    #         user_profile_serializer.save()
    #         return Response({**user_serializer.data,
    #                         **user_profile_serializer.data})
    #     return Response(user_serializer.errors,
    #                     status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk, format=None):
    #     user = self.get_object(pk)
    #     user.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)




class User_Question_Detail_class(APIView):
    def get(self, request, pk, format=None):
        questions = Question.objects.filter(author_id=pk).all()
        serializer = QuestionSerializer(questions, context={'request': request},
                                    many=True)
        return Response(serializer.data)



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
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)

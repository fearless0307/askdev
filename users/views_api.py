from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from rest_framework import request, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from questions.models import Question
from questions.serializers import QuestionSerializer
from users.models import Profile, FavouriteQuestion
from users.serializers import UserSerializer, FavouriteQuestionSerializer,\
    ProfileSerializer


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
        profile = Profile.objects.filter(user_id=pk).first()
        if profile is not None:
            profile_serializer =\
                ProfileSerializer(profile, context={'request': request})
            return \
                Response({**user_serializer.data, **profile_serializer.data})
        else:
            return Response(user_serializer.data)


class User_Question_Detail_class(APIView):
    def get(self, request, pk, format=None):
        questions = Question.objects.filter(author_id=pk).all()
        serializer =\
            QuestionSerializer(questions, context={'request': request},
                               many=True)
        return Response(serializer.data)


class User_FavouriteQuestion_Detail(APIView):
    def get(self, request, pk, format=None):
        qid = FavouriteQuestion.objects.values_list(
            'question_id', flat=True).filter(author_id=pk).all()
        questions = Question.objects.filter(id__in=qid).all()
        serializer = QuestionSerializer(questions,
                                        context={'request': request},
                                        many=True)
        return Response(serializer.data)

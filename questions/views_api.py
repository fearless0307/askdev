from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.urls import reverse
from django.db.models import Q

from rest_framework import request, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from stories.models import StoryTag
from stories.serializers import StoryTagSerializer
from questions.models import Question, Reply, QuestionReaction, Tag,\
    QuestionTag, Answer, Reaction
from questions.serializers import QuestionSerializer, AnswerSerializer,\
    ReplySerializer, QuestionReactionSerializer, TagSerializer,\
    ReactionSerializer,  QuestionTagSerializer, TagDataSerializer


def all_api(request):
    html = "<html><body><ul>"\
           "<h1>All APIs</h1>"\
           "<li><h3><a href="+reverse('users')+">Users</a></h3></li>"\
           "<li><h3><a href="+reverse('questions')+">Questions</a></h3></li>"\
           "<li><h3><a href="+reverse('story-list')+">Stories</a></h3></li>"\
           "<li><h3><a href="+reverse('reactions')+">Reactions</a></h3></li>"\
           "<li><h3><a href="+reverse('tag')+">Tags</a></h3></li>"\
           "</ul></body></html>"
    return HttpResponse(html)


class Question_class(APIView):

    def get(self, request, format=None):
        search = request.GET.get('search', '')
        if search == '':
            question = Question.objects.all()
        else:
            question = Question.objects.filter(Q(question__icontains=search)|Q(author__username__icontains=search)).all()
        serializer = QuestionSerializer(question,
                                        context={'request': request},
                                        many=True)
        return Response(serializer.data)


class Question_Detail_class(APIView):
    def get_object(self, pk):
        try:
            return Question.objects.get(id=pk)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = QuestionSerializer(question, context={'request': request})
        return Response(serializer.data)


class Reply_detail(APIView):
    def get_object(self, pk):
        try:
            return Reply.objects.filter(id=pk).first()
        except Reply.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        reply = self.get_object(pk)
        serializer = ReplySerializer(reply, context={'request': request})
        return Response(serializer.data)


# class QuestionReaction_list(APIView):
#     def get(self, request, pk, format=None):
#         reaction = QuestionReaction.objects.filter(question_id=pk).all()
#         serializer = QuestionReactionSerializer(reaction,
#                                                 context={'request': request},
#                                                 many=True)
#         return Response(serializer.data)


# class QuestionReaction_detail(APIView):
#     def get_object(self, pk):
#         try:
#             return QuestionReaction.objects.filter(pk=pk).first()
#         except QuestionReaction.DoesNotExist:
#             return Http404

#     def get(self, request, pk, format=None):
#         reaction = self.get_object(pk)
#         serializer = QuestionReactionSerializer(reaction,
#                                                 context={'request': request})
#         return Response(serializer.data)


class Tags_list(APIView):
    def get(self, request, format=None):
        tags = Tag.objects.all()
        serializer = TagSerializer(
            tags, many=True, context={'request': request})
        return Response(serializer.data)


class Tags_data_list(APIView):
    def get(self, request, format=None):
        tags = Tag.objects.all()
        serializer = TagDataSerializer(tags, many=True)
        return Response(serializer.data)


class Tags_detail(APIView):
    def get_object(self, name):
        try:
            return Tag.objects.get(name=name)
        except Tag.DoesNotExist:
            return Http404

    def get(self, request, name, format=None):
        tags = self.get_object(name)
        serializer = TagSerializer(tags, context={'request': request})
        return Response(serializer.data)


class Tags_questions(APIView):
    def get(self, request, name, format=None):
        questions_tag = QuestionTag.objects.filter(tag__name=name).all()
        serializer = QuestionTagSerializer(questions_tag,
                                           context={'request': request},
                                           many=True)
        return Response(serializer.data)


class Answer_list(APIView):
    def get(self, request, pk, format=None):
        answer = Answer.objects.filter(question_id=pk).all()
        serializer = AnswerSerializer(answer,
                                      context={'request': request},
                                      many=True)
        return Response(serializer.data)


class Answer_detail(APIView):
    def get_object(self, pk, qid):
        try:
            return Answer.objects.filter(pk=pk, question_id=qid).first()
        except Answer.DoesNotExist:
            return Http404

    def get(self, request, pk, qid, format=None):
        answer = self.get_object(pk, qid)
        serializer = AnswerSerializer(answer, context={'request': request})
        return Response(serializer.data)


class Reaction_list(APIView):
    def get(self, request, format=None):
        reaction = Reaction.objects.all()
        serializer = ReactionSerializer(reaction, context={'request': request},
                                        many=True)
        return Response(serializer.data)


class Reaction_detail(APIView):
    def get_object(self, pk):
        try:
            return Reaction.objects.filter(pk=pk).first()
        except Reaction.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):

        print("get", pk)
        reaction = self.get_object(pk)
        serializer = ReactionSerializer(reaction, context={'request': request})
        return Response(serializer.data)

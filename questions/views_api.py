from django.shortcuts import render
from questions.models import Question, Reply, QuestionReaction, Tag,\
    QuestionTag, Answer, Reaction
from questions.serializers import QuestionSerializer, AnswerSerializer,\
    ReplySerializer, QuestionReactionSerializer, TagSerializer,\
    ReactionSerializer,  QuestionTagSerializer
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework import request, status
from rest_framework.views import APIView
from rest_framework.response import Response


class Question_class(APIView):

    def get(self, request, format=None):
        question = Question.objects.all()
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


class Reply_list(APIView):
    def get(self, request, qid, pk, format=None):
        reply = Reply.objects.filter(answer_id=pk).all()
        serializer = ReplySerializer(reply,context={'request': request},many=True)
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


class QuestionReaction_list(APIView):
    def get(self, request, pk, format=None):

        reaction = QuestionReaction.objects.filter(question_id=pk).all()
        print("reaction =", pk, reaction)
        serializer = QuestionReactionSerializer(reaction,
                                                context={'request': request},
                                                many=True)
        return Response(serializer.data)


class QuestionReaction_detail(APIView):
    def get_object(self, pk):
        try:
            return QuestionReaction.objects.filter(pk=pk).first()
        except QuestionReaction.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        reaction = self.get_object(pk)
        serializer = QuestionReactionSerializer(reaction,
                                                context={'request': request})
        return Response(serializer.data)


class Tags_list(APIView):
    def get(self, request, format=None):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)


class Tags_detail(APIView):
    def get_object(self, pk):
        try:
            return Tag.objects.get(pk=pk)
        except Tag.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        tags = Tag.objects.get(pk=pk)
        serializer = TagSerializer(tags)
        return Response(serializer.data)


class QuestionTag_list(APIView):
    def get(self, request, pk, format=None):
        question_tag = QuestionTag.objects.filter(question_id=pk).all()
        serializer = QuestionTagSerializer(question_tag, context={'request': request},  many=True)
        return Response(serializer.data)


class QuestionTag_detail(APIView):
    def get_object(self, pk):
        try:
            return QuestionTag.objects.get(pk=pk)
        except QuestionTag.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        question_tag = self.get_object(pk)
        serializer = QuestionTagSerializer(question_tag)
        return Response(serializer.data)

class Tags_questions(APIView):
   def get(self, request, pk, format=None):
       qid = QuestionTag.objects.values_list('question_id', flat=True).filter(tag_id=pk).all()
       questions = Question.objects.filter(id__in=qid).all()
    #    print("auhot_tag=",qid,questions)
       serializer = QuestionSerializer(questions, context={'request': request},
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

        print("get", pk)
        answer = self.get_object(pk, qid)
        serializer = AnswerSerializer(answer, context={'request': request},)
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

from django.shortcuts import render
from rest_framework import generics

from quizes.models import Question
from quizes.serializers import QuestionSerializer


class QuestionsList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

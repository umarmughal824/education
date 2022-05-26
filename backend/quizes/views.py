from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response




from quizes.models import Question
from quizes.serializers import QuestionSerializer, CreateQuizSerializer


class QuestionsList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class CreateQuiz(APIView):
    def post(self, request):
        serializer = CreateQuizSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response('Quiz created successfully', status=status.HTTP_200_OK)
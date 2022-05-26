from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response




from quizes.models import Question, Quiz
from quizes.serializers import QuestionSerializer, CreateQuizSerializer, QuizSerializer, QuizDetailSerializer


class QuestionsList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class CreateQuiz(APIView):
    def post(self, request):
        print('request.data')
        print(request.data)
        serializer = CreateQuizSerializer(data=request.data)


        if serializer.is_valid():
            print('serializer is valid')
            serializer.save()
        else:
            print('serializer is not valid')
            print(serializer.errors)

        return Response('Quiz created successfully', status=status.HTTP_200_OK)


class QuizesList(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuizRetrieve(generics.RetrieveAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizDetailSerializer

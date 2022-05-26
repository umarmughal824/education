from django.urls import path

from quizes.views import QuestionsList, CreateQuiz, QuizesList, QuizRetrieve


urlpatterns = [
    path('questions/', QuestionsList.as_view(), name='questions'),
    path('create-quiz/', CreateQuiz.as_view(), name='create-quiz'),
    path('allquizes/', QuizesList.as_view(), name='quizes'),
    path('allquizes/<int:pk>/', QuizRetrieve.as_view(), name='quiz_details'),

]

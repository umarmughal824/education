from django.urls import path

from quizes.views import QuestionsList, CreateQuiz


urlpatterns = [
    path('questions/', QuestionsList.as_view(), name='questions'),
    path('create-quiz/', CreateQuiz.as_view(), name='create-quiz'),
]

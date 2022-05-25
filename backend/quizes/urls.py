from django.urls import path

from quizes.views import QuestionsList


urlpatterns = [
    path('questions/', QuestionsList.as_view(), name='questions')
]
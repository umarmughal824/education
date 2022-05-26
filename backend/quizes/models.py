from django.db import models


class Quiz(models.Model):
    name = models.CharField(max_length=100)


class Question(models.Model):
    category = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    difficulty = models.CharField(max_length=20)
    text = models.TextField()
    correct_answer = models.CharField(max_length=250)
    incorrect_answer = models.TextField()


class QuizQuestions(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('quiz', 'question')

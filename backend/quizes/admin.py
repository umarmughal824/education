from django.contrib import admin

from quizes.models import Quiz, Question


class QuizAdmin(admin.ModelAdmin):
    model = Quiz


class QuestionAdmin(admin.ModelAdmin):
    model = Question

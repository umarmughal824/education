from rest_framework import serializers

from quizes.models import Question, Quiz, QuizQuestions


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class CreateQuizSerializer(serializers.Serializer):
    def validate(self, attrs):
        name = attrs.get('name', None)
        questions = attrs.get('questions', None)

        if not name:
            raise serializers.ValidationError("Name is required")

        if not questions:
            raise serializers.ValidationError("Questions are required")

        return attrs


    def create(self, validated_data):
        name = validated_data.get('name')
        questions = validated_data.get('questions')
        questions = questions.split(',')

        quiz = Quiz.objects.create(name=name)
        for question in questions:
            QuizQuestions.objects.create(quiz=quiz, questions_id=int(question))


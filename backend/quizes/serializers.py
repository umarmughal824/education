from rest_framework import serializers

from quizes.models import Question, Quiz, QuizQuestions


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class QuizQuestionSerialzer(serializers.ModelSerializer):
    question = serializers.HyperlinkedRelatedField(read_only=True, view_name='question-detail')
    class Meta:
        model = QuizQuestions
        fields = 'question'



class QuizDetailSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()
    class Meta:
        model = Quiz
        fields = '__all__'

    def get_questions(self, instance):
        quizQues = QuizQuestions.objects.filter(quiz=instance)
        return [QuestionSerializer(quizQue.question).data for quizQue in quizQues]


class CreateQuizSerializer(serializers.Serializer):
    name = serializers.CharField()
    questions = serializers.CharField()

    def validate(self, attrs):
        print('attrs', attrs)
        name = attrs.get('name', None)
        questions = attrs.get('questions', None)

        
        if not name:
            raise serializers.ValidationError("Name is required")

        if not questions:
            raise serializers.ValidationError("Questions are required")

        return attrs


    def create(self, validated_data):
        print('validated_data', validated_data)
        name = validated_data.get('name')
        questions = validated_data.get('questions')
        questions = questions.split(',')

        quiz = Quiz.objects.create(name=name)
        for question in questions:
            QuizQuestions.objects.create(quiz=quiz, question_id=int(question))
        return quiz

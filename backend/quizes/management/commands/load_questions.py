import requests
import json

from django.core.management.base import BaseCommand, CommandError
from quizes.models import Question


class Command(BaseCommand):
    help = 'It imports the template questions'

    def add_argument(self, parser):
        pass

    def handle(self, *args, **kwargs):
        response = requests.get('https://opentdb.com/api.php?amount=20&category=9')
        if response.status_code == 200:
            response = response.json()
            results = response['results']
            for result in results:
                print(result)
                question = Question(
                    category=result['category'],
                    type=result['type'],
                    difficulty=result['difficulty'],
                    text=result['question'],
                    correct_answer=result['correct_answer'],
                    incorrect_answer=result['incorrect_answers'],
                )
                question.save()
        else:
            raise CommandError("Url did not respond as per our expectation")

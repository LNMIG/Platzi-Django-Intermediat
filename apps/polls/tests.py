import datetime

from django.test import TestCase
from django.utils import timezone

from apps.polls.models import Question


# Create your tests here.
class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_questions(self):
        '''
        function "was_pusblished_recently" returns False for
        questions which "pub_date" is in the future.
        '''
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text="¿Quién es el mejor profesor de Platzi?", pub_date=time)
        self.assertIs(future_question.was_published_recentrly(), False)
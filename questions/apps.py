from django.apps import AppConfig
import sys

sys.path.append("..")


class QuestionsConfig(AppConfig):
    name = 'questions'

    def ready(self):
        from questions import signals

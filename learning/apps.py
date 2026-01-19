from django.apps import AppConfig

class LearningConfig(AppConfig):
    name = 'learning'

    def ready(self):
        import learning.signals

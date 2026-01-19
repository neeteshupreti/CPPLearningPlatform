from django.contrib import admin
from .models import Chapter, Quiz, Question, UserAnswer
from django.contrib.admin.sites import AlreadyRegistered

# Safely register models
for model in [Chapter, Quiz, Question, UserAnswer]:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass

from django.contrib import admin
from .models import Question, Option

class OptionInline(admin.TabularInline):
    model = Option
    extra = 3 # Shows 3 empty slots by default

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('order', 'story')
    inlines = [OptionInline]
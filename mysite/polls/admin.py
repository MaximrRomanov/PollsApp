from django.contrib import admin

# Register your models here.
from .models import Question, Choice


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "published_at"
    )


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'question',
        'votes'
    )

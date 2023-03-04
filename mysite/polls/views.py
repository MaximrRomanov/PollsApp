from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Question


def index(request):
    latest_questions_list = Question.objects.order_by('-published_at')[:5]
    context = {
        'latest_questions_list': latest_questions_list
    }
    return render(request, 'polls/index.html', context)
    # Этот код загружает шаблон с именем polls/index.html и передает ему контекст.
    # Контекст представляет собой словарь, отображающий имена переменных шаблона в объекты Python
    # Функция render() принимает объект запроса в качестве первого аргумента, имя шаблона в качестве второго аргумента и
    # словарь в качестве необязательного третьего аргумента.
    # Она возвращает объект HttpResponse данного шаблона, отображенный в данном контексте


def details(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

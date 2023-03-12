from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
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


# def details(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404('Question does not exist')
#     return render(request, 'polls/details.html', {'question': question})
# Новая концепция:
# представление вызывает исключение Http404,
# если вопрос с запрошенным идентификатором не существует.


def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/details.html', {'question': question})
    # Функция get_object_or_404() принимает модель Django в качестве первого аргумента
    # и произвольное количество ключевых аргументов, которое она передает в Http404(),
    # если объект не существует. Также есть функция get_list_or_404(),
    # которая работает так же, как get_object_or_404() - за исключением использования filter()


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

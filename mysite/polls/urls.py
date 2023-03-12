from django.urls import path

from . import views

# добавьте app_name для установки пространства имен приложения
app_name = 'polls'

# список роутов/маршрутов/урлов
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # функция path
    # первый параметр - шаблонный путь,
    # второй параметр - путь(ссылка на котроллер-функцию)


    # ex: /polls/5/   the 'name' value as called by the {% url %} template tag
    path('<int:question_id>/', views.details, name="details"),
    # ex: /polls/5/results/   the 'name' value as called by the {% url %} template tag
    path('<int:question_id>/results/', views.results, name="results"),
    # ex: /polls/5/vote/   the 'name' value as called by the {% url %} template tag
    path('<int:question_id>/vote/', views.vote, name="vote")
]

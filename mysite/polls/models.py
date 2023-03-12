import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    # переменная класса = поле базы данных в модели
    question = models.CharField(
        verbose_name="Вопрос", max_length=255
    )
    # каждое поле представлено экземпляром класса Field
    # переменная класса = поле базы данных в модели
    published_at = models.DateTimeField(
        default=timezone.now, verbose_name="Когда опубликован"
    )

    # каждое поле представлено экземпляром класса Field

    def __str__(self):
        return self.question

    def was_published_recently(self):
        return self.published_at >= (timezone.now() - datetime.timedelta(days=1)).timestamp()  #

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Choice(models.Model):
    # переменная класса = поле базы данных в модели
    question = models.ForeignKey(
        Question, verbose_name="Вопрос", on_delete=models.CASCADE
    )
    # каждое поле представлено экземпляром класса Field
    # переменная класса = поле базы данных в моделиru
    text = models.CharField(
        verbose_name="Текст выбора", max_length=255
    )
    # каждое поле представлено экземпляром класса Field
    # переменная класса = поле базы данных в модели
    votes = models.PositiveIntegerField(
        verbose_name="Подсчитанные голоса"
    )
    # каждое поле представлено экземпляром класса Field

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
# Миграции - это то, как Django хранит изменения в ваших моделях (и, следовательно, в вашей схеме базы данных) - это
# файлы на диске.


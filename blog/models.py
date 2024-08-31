from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.CharField(max_length=50, verbose_name='Автор')
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст поста')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Опубликовано', editable=False)

    class Meta:
        # Имя таблицы в единственном числе
        verbose_name = 'Пост'
        # Имя таблици во множественном числе
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title
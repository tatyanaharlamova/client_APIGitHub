from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Git(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название репозитория', help_text='формат: имя_владельца/название')
    url = models.URLField(verbose_name='URL')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    class Meta:
        verbose_name = 'Гит'
        verbose_name_plural = 'Гит'

    def __str__(self):
        return f'{self.name}'


class Commit(models.Model):
    sha = models.CharField(max_length=150, verbose_name='sha')
    url = models.URLField(verbose_name='URL')
    author = models.EmailField(verbose_name='Емайл автора', **NULLABLE)
    date = models.DateTimeField(verbose_name='Дата и время')
    comments = models.TextField(verbose_name='Коментарий', **NULLABLE)
    git = models.ForeignKey(Git, on_delete=models.CASCADE, verbose_name='Гит')

    class Meta:
        verbose_name = 'Коммит'
        verbose_name_plural = 'Коммиты'

    def __str__(self):
        return f'{self.url}'

from datetime import time

from django.db import models


class MailSand(models.Model):
    STATUS_CHOICES = [
        (1, 'Создана'),
        (2, 'Запущена'),
        (3, 'Завершена'),
    ]

    PERIOD_CHOICES = [
        ('daily', 'Ежедневно'),
        ('weekly', 'Еженедельно'),
        ('monthly', 'Ежемесячно'),
    ]

    name = models.CharField(max_length=150, verbose_name='Название рассылки')
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=1, verbose_name='Статус рассылки')
    period = models.CharField(max_length=10, choices=PERIOD_CHOICES, default='daily', verbose_name='Периодичность')
    start_sand = models.TimeField(default=time(hour=10), verbose_name='Время начала рассылки')
    end_send = models.TimeField(default=time(hour=11), verbose_name='Время окончания рассылки')
    name_mail = models.CharField(max_length=150, verbose_name='Тема письма')
    text_mail = models.TextField(verbose_name='Текст письма')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        ordering = ['-pk']


class Client(models.Model):
    full_name = models.CharField(max_length=300, verbose_name='Ф.И.О.')
    client_email = models.EmailField(unique=True, verbose_name='Почта клиента')
    comment = models.TextField(null=True, blank=True, verbose_name='Комментарий')

    def __str__(self):
        return f'{self.full_name} ({self.client_email})'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиеты'


# class MailText(models.Model):
#     name = models.ForeignKey('MailSand', on_delete=models.CASCADE, verbose_name='Название рассылки')
#
#     name_mail = models.CharField(max_length=150, verbose_name='Тема письма')
#     text_mail = models.TextField(verbose_name='Тело письма')
#
#     def __str__(self):
#         return f'{self.name_mail}'
#
#     class Meta:
#         verbose_name = 'Письмо'
#         verbose_name_plural = 'Письма'


class EmailLog(models.Model):
    name = models.ForeignKey('MailSand', on_delete=models.CASCADE, verbose_name='Название рассылки')
    server_response = models.TextField(verbose_name='Ответ почтового сервера')
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время последней попытки')
    status = models.CharField(max_length=10, verbose_name='Статус отправки')

    def __str__(self):
        return f'{self.sent_at}, {self.status}'

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'

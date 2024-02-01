from datetime import time

from django.db import models

from users.models import User


class Client(models.Model):
    full_name = models.CharField(max_length=300, verbose_name='Ф.И.О.')
    client_email = models.EmailField(verbose_name='Почта клиента')
    comment = models.TextField(null=True, blank=True, verbose_name='Комментарий')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец')

    def __str__(self):
        return f'{self.full_name} ({self.client_email})'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        unique_together = (('owner', 'client_email',),)


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
    last_sent = models.DateTimeField(null=True, blank=True, verbose_name='Дата последней отправки письма')
    owner = models.ManyToManyField(Client, verbose_name='Клиенты')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        ordering = ['-pk']

        permissions = [
            (
                'set_status',
                'can_deactivate_send'
            )
        ]


class EmailLog(models.Model):
    STATUS_CHOICES = [
        (1, 'Успешно'),
        (2, 'Не успешно'),
    ]

    mail = models.ForeignKey('MailSand', on_delete=models.CASCADE, verbose_name='Название рассылки')
    server_response = models.TextField(verbose_name='Ответ почтового сервера')
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время последней попытки')
    status = models.CharField(choices=STATUS_CHOICES, max_length=20, verbose_name='Статус отправки')

    def __str__(self):
        return f'{self.sent_at}, {self.status}'

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'

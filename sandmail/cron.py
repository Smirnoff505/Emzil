from django.conf import settings
from django.core.mail import send_mail
from django.db.models import QuerySet

from sandmail.models import Client, MailSand


def send_daily():
    """Функция отправки писем по расписанию"""
    mails: QuerySet = Client.objects.all()
    list_address = [mail for mail in mails.values_list('client_email', flat=True)]
    all_mail = MailSand.objects.all()
    for mail in all_mail:
        if mail.period == 'daily':
            send_mail(
                subject=mail.name_mail,
                message=mail.text_mail,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=list_address
            )


# def send_weekly():
#     """Функция отправки писем раз в неделю"""
#     pass
#
#
# def send_monthly():
#     """Функция отправки писем раз в месяц"""
#     pass

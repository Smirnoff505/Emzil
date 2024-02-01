from django.conf import settings

from django.core.mail import send_mail
from django.utils import timezone

from sandmail.models import MailSand, EmailLog


def send_daily():
    """Функция отправки писем по расписанию"""
    current_time = timezone.now().time()
    mails = MailSand.objects.filter(period='daily', status=2)
    for mail in mails:
        if mail.start_sand <= current_time <= mail.end_send and (
                mail.last_sent is None or mail.last_sent.date() != timezone.now().date()):
            email_list = []
            for client in mail.owner.all():
                email_list.append(client.client_email)
            try:
                result = send_mail(
                    subject=mail.name_mail,
                    message=mail.text_mail,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=email_list,
                )
                EmailLog.objects.create(mail=mail, server_response=bool(result), status=EmailLog.STATUS_CHOICES[0][1])
            except Exception as e:
                EmailLog.objects.create(mail=mail, server_response=e, status=EmailLog.STATUS_CHOICES[1][1])
            finally:
                mail.last_sent = timezone.now()
                mail.save()


def send_weekly():
    """Функция отправки писем раз в неделю"""
    current_time = timezone.now().time()
    mails = MailSand.objects.filter(period='weekly', status=2)
    for mail in mails:
        if mail.start_sand <= current_time <= mail.end_send and (
                mail.last_sent is None or mail.last_sent < timezone.now() - timezone.timedelta(days=7)):
            email_list = []
            for client in mail.owner.all():
                email_list.append(client.client_email)
            try:
                result = send_mail(
                    subject=mail.name_mail,
                    message=mail.text_mail,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=email_list,
                )
                EmailLog.objects.create(mail=mail, server_response=bool(result), status=EmailLog.STATUS_CHOICES[0][1])
            except Exception as e:
                EmailLog.objects.create(mail=mail, server_response=e, status=EmailLog.STATUS_CHOICES[1][1])
            finally:
                mail.last_sent = timezone.now()
                mail.save()


#
#
def send_monthly():
    """Функция отправки писем раз в месяц"""
    current_time = timezone.now().time()
    mails = MailSand.objects.filter(period='monthly', status=2)
    for mail in mails:
        if mail.start_sand <= current_time <= mail.end_send and (
                mail.last_sent is None or mail.last_sent < timezone.now() - timezone.timedelta(days=30)):
            email_list = []
            for client in mail.owner.all():
                email_list.append(client.client_email)
            try:
                result = send_mail(
                    subject=mail.name_mail,
                    message=mail.text_mail,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=email_list,
                )
                EmailLog.objects.create(mail=mail, server_response=bool(result), status=EmailLog.STATUS_CHOICES[0][1])
            except Exception as e:
                EmailLog.objects.create(mail=mail, server_response=e, status=EmailLog.STATUS_CHOICES[1][1])
            finally:
                mail.last_sent = timezone.now()
                mail.save()

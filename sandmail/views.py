from datetime import datetime

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blog.models import Blog
from sandmail.models import MailSand, Client


def home(request):
    client_count = Client.objects.count()
    mailsand_count = MailSand.objects.count()
    mailsand_count_active = MailSand.objects.filter(status=2).count()
    mailsand_count_notactive = MailSand.objects.filter(status=3).count()
    blog_random = Blog.objects.order_by('?')[:3]
    context = {'client_count': client_count,
               'mailsand_count': mailsand_count,
               'mailsand_count_active': mailsand_count_active,
               'mailsand_count_notactive': mailsand_count_notactive,
               'blog_random': blog_random}

    return render(request, 'sandmail/home.html', context)


class MailSandCreateView(CreateView):
    model = MailSand
    fields = ('name', 'period', 'start_sand', 'end_send', 'name_mail', 'text_mail',)
    success_url = reverse_lazy('sandmail:list')

    def form_valid(self, form):
        # получаем email из модели Client через list comprehension формируем список
        mails = Client.objects.all()
        list_mail = [mail for mail in mails.values_list('client_email', flat=True)]
        # Проверяем, что время начала рассылки меньше времени окончания рассылки
        if datetime.now().time() > form.instance.start_sand and datetime.now().time() < form.instance.end_send:
            # Отправляем письмо
            send_mail(
                subject=form.instance.name_mail,
                message=form.instance.text_mail,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=list_mail
            )
            # Изменяем статус рассылки
            form.instance.status = 2
        return super().form_valid(form)


class MailSandUpdateView(UpdateView):
    model = MailSand
    fields = ('name', 'period', 'start_sand', 'end_send', 'name_mail', 'text_mail',)
    success_url = reverse_lazy('sandmail:list')


class MailSandListView(ListView):
    """Просмотр всех сущности из модели"""
    model = MailSand


class MailSandDetailView(DetailView):
    """Просмотр одной сущности из модели"""
    model = MailSand


class MailSandDeleteView(DeleteView):
    """Удаление сущности"""
    model = MailSand
    success_url = reverse_lazy('sandmail:list')


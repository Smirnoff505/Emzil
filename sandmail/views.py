from django.conf import settings
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.core.cache import cache
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blog.models import Blog
from sandmail.forms import MailSandForm
from sandmail.models import MailSand, Client, EmailLog


# def home(request):
#     client_count = Client.objects.count()
#     mailsand_count = MailSand.objects.count()
#     mailsand_count_active = MailSand.objects.filter(status=2).count()
#     mailsand_count_notactive = MailSand.objects.filter(status=3).count()
#     blog_random = Blog.objects.order_by('?')[:3]
#     context = {'client_count': client_count,
#                'mailsand_count': mailsand_count,
#                'mailsand_count_active': mailsand_count_active,
#                'mailsand_count_notactive': mailsand_count_notactive,
#                'blog_random': blog_random}
#
#     return render(request, 'sandmail/home.html', context)

def home(request):
    if settings.CACHE_ENABLED:
        key = str([Client.objects.count(), MailSand.objects.count(), MailSand.objects.filter(status=2).count(),
                          MailSand.objects.filter(status=3).count()])
        cache_list = cache.get(key)
        if cache_list is None:
            cache_list = [Client.objects.count(), MailSand.objects.count(), MailSand.objects.filter(status=2).count(),
                      MailSand.objects.filter(status=3).count()]
            cache.set(key, cache_list)
        else:
            client_count = cache_list[0]
            mailsand_count = cache_list[1]
            mailsand_count_active = cache_list[2]
            mailsand_count_notactive = cache_list[3]
    blog_random = Blog.objects.order_by('?')[:3]
    context = {'client_count': client_count,
               'mailsand_count': mailsand_count,
               'mailsand_count_active': mailsand_count_active,
               'mailsand_count_notactive': mailsand_count_notactive,
               'blog_random': blog_random}
    return render(request, 'sandmail/home.html', context)


class MailSandCreateView(LoginRequiredMixin, CreateView):
    model = MailSand
    form_class = MailSandForm
    success_url = reverse_lazy('sandmail:list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class MailSandUpdateView(LoginRequiredMixin, UpdateView):
    model = MailSand
    fields = ('name', 'period', 'start_sand', 'end_send', 'name_mail', 'text_mail', 'owner',)
    success_url = reverse_lazy('sandmail:list')


class MailSandListView(LoginRequiredMixin, ListView):
    """Просмотр всех сущности из модели"""
    model = MailSand


class MailSandDetailView(LoginRequiredMixin, DetailView):
    """Просмотр одной сущности из модели"""
    model = MailSand


class MailSandDeleteView(LoginRequiredMixin, DeleteView):
    """Удаление сущности"""
    model = MailSand
    success_url = reverse_lazy('sandmail:list')


class CreateClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    fields = ('full_name', 'client_email', 'comment',)
    success_url = reverse_lazy('sandmail:home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    fields = ('full_name', 'client_email', 'comment',)
    success_url = reverse_lazy('sandmail:home')


class ListClientListView(LoginRequiredMixin, ListView):
    model = Client


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('sandmail:home')


@login_required
# @permission_required('sandmail.set_status')
def status(request, pk):
    """Смена статуса """
    stat = MailSand.objects.get(pk=pk)
    if stat.status == 1:
        stat.status = 2
    elif stat.status == 2:
        stat.status = 3
    stat.save()
    return redirect(reverse('sandmail:detail', args=[pk]))


class LogListView(LoginRequiredMixin, ListView):
    model = EmailLog

    # def test_func(self):
    #     return self.user.is_staff

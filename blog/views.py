from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from blog.models import Blog


class BlogCreateView(PermissionRequiredMixin, CreateView):
    """Создание сущности с полями:
    title: str
    body: text
    preview: img"""
    model = Blog
    fields = ('title', 'body', 'preview',)
    permission_required = 'blog.add_blog'
    success_url = reverse_lazy('blog:list')


class BlogUpdateView(PermissionRequiredMixin, UpdateView):
    """Update существующей сущности"""
    model = Blog
    fields = ('title', 'body', 'preview',)
    permission_required = 'blog.change_blog'

    def get_success_url(self):
        """Переопределен метод, для перенаправления на статью после обновления."""
        return reverse('blog:detail', args=[self.object.pk])


class BlogListView(ListView):
    """Просмотр всех сущностей модели"""
    model = Blog


class BlogDetailView(DetailView):
    """Просмотр одной сущности из модели"""
    model = Blog

    def get_object(self, queryset=None):
        """Переопределение метода для подсчета количества просмотров"""
        self.object = super().get_object(queryset)
        # Счетчик просмотров
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogDeleteView(PermissionRequiredMixin, DeleteView):
    """Удаление объекта"""
    model = Blog
    permission_required = 'blog.delete_blog'
    success_url = reverse_lazy('blog:list')

from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from blog.models import Blog


class BlogCreateView(CreateView):
    """Создание сущности с полями:
    title: str
    body: text
    preview: img"""
    model = Blog
    fields = ('title', 'body', 'preview',)
    success_url = reverse_lazy('blog:list')


class BlogUpdateView(UpdateView):
    """Update существующей сущности"""
    model = Blog
    fields = ('title', 'body', 'preview',)

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


class BlogDeleteView(DeleteView):
    """Удаление объекта"""
    model = Blog
    success_url = reverse_lazy('blog:list')

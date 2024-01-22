from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Статья')
    preview = models.ImageField(upload_to='imj_blog/', verbose_name='Изображение', null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    views_count = models.IntegerField(verbose_name='Количество просмотров', default=0)

    def __str__(self):
        return f'{self.title}, {self.create_date}'

    class Meta:
        verbose_name = 'Блог'

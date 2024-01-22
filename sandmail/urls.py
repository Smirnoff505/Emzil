from django.urls import path

from sandmail.apps import SandmailConfig
from sandmail.views import home, MailSandCreateView, MailSandListView, MailSandDetailView, MailSandUpdateView, \
    MailSandDeleteView

app_name = SandmailConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('create/', MailSandCreateView.as_view(), name='create'),
    path('list/', MailSandListView.as_view(), name='list'),
    path('detail/<int:pk>', MailSandDetailView.as_view(), name='detail'),
    path('update/<int:pk>', MailSandUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', MailSandDeleteView.as_view(), name='delete'),
]

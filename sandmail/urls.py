from django.urls import path

from sandmail.apps import SandmailConfig
from sandmail.views import home, MailSandCreateView, MailSandListView, MailSandDetailView, MailSandUpdateView, \
    MailSandDeleteView, CreateClientCreateView, status, ListClientListView, ClientUpdateView, ClientDeleteView, LogListView

app_name = SandmailConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('create/', MailSandCreateView.as_view(), name='create'),
    path('list/', MailSandListView.as_view(), name='list'),
    path('detail/<int:pk>/', MailSandDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', MailSandUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', MailSandDeleteView.as_view(), name='delete'),
    path('create/client/', CreateClientCreateView.as_view(), name='create_client'),
    path('update/client/<int:pk>', ClientUpdateView.as_view(), name='update_client'),
    path('list/client/', ListClientListView.as_view(), name='list_client'),
    path('delete/client/<int:pk>', ClientDeleteView.as_view(), name='delete_client'),
    path('status/<int:pk>/', status, name='activate_or_deactivate'),
    path('loglist/', LogListView.as_view(), name='loglist_view'),
]

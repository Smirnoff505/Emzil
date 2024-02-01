from django.contrib import admin

from sandmail.models import MailSand, Client, EmailLog


@admin.register(MailSand)
class MailSandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'start_sand', 'end_send', 'status', )
    list_filter = ('name', 'status', 'period',)
    search_fields = ('name',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'client_email', 'owner',)
    list_filter = ('full_name',)


@admin.register(EmailLog)
class EmailLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'mail', 'status', 'server_response', 'sent_at',)
    list_filter = ('status',)
    search_fields = ('sent_at',)

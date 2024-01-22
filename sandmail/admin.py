from django.contrib import admin

from sandmail.models import MailSand, Client, EmailLog


@admin.register(MailSand)
class MailSandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'start_sand', 'end_send',)
    list_filter = ('name', 'status', 'period',)
    search_fields = ('name',)


# @admin.register(MailText)
# class MailTextAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'name_mail',)
#     search_fields = ('name', 'name_mail',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'client_email',)
    list_filter = ('full_name',)


@admin.register(EmailLog)
class EmailLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'sent_at',)
    list_filter = ('status',)
    search_fields = ('sent_at',)

from django import forms

from sandmail.models import MailSand, Client


class MailSandForm(forms.ModelForm):
    class Meta:
        model = MailSand
        exclude = ('last_sent',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(MailSandForm, self).__init__(*args, **kwargs)
        if user is not None:
            self.fields['owner'].queryset = Client.objects.filter(owner=user)


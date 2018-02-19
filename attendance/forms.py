from django import forms
from .models import Event
from member.models import Member


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ('club', )

    def __init__(self, club, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['absent_member'].queryset = Member.objects.filter(club=club).values_list('user__username', flat=True)


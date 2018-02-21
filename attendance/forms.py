from django import forms
from .models import Event
from member.models import Member


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ('club', )

    def __init__(self, club, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        members = Member.objects.filter(club=club)
        self.fields['absent_member'].choices = [(str(i+1), members[i].user.username) for i in range(len(members))]

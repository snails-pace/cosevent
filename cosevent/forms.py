from django import forms
from django.core.exceptions import ValidationError

from cosevent.models import Event, User


class DateInput(forms.DateInput):
    input_type = 'date'


class CustomModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, user):
        return user.username


class UpdateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'venue', 'category', 'availability', 'artist_name']

        widgets = {
            'date': DateInput()
        }

        owner = CustomModelChoiceField(
            queryset=User.objects.all(),
            widget=forms.Select(attrs={'class': 'form-control'}),
            to_field_name='username',
            label='Owner'
        )


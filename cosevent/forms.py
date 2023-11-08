from django import forms
from django.core.exceptions import ValidationError

from cosevent.models import Event

class DateInput(forms.DateInput):
    input_type = 'date'


class CustomModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, event):
        return event.id


class UpdateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['id', 'name', 'date', 'venue', 'category', 'availability', 'artist_name']

        widgets = {
            'date': DateInput()
        }

        def clean_name(self):
            name = self.cleaned_data['name']

            if name.length < 0:
                raise ValidationError("The name must have at least one character")
            return name
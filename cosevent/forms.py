from django import forms
from django.core.exceptions import ValidationError

from cosevent.models import Event, User


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class CustomModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, user):
        return user.username


class UpdateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'venue', 'category', 'availability', 'artist_name']

        widgets = {
            'date': DateTimeInput()
        }

        def clean_name(self):
            name = self.cleaned_data['name']
            if name.isEmpty():
                raise ValidationError("The name is required!")

        # owner = CustomModelChoiceField(
        #     queryset=User.objects.all(),
        #     widget=forms.Select(attrs={'class': 'form-control'}),
        #     to_field_name='username',
        #     label='Owner'
        # )


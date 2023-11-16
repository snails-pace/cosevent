from django import forms
from django.core.exceptions import ValidationError

from cosevent.models import Event, Category


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

    def clean_date(self):
        input_date = self.cleaned_data['date']

        events = Event.objects.filter(date__date=input_date.date())
        if events:
            raise ValidationError("Sorry, the venue is booked at this date!")
        return input_date


        # owner = CustomModelChoiceField(
        #     queryset=User.objects.all(),
        #     widget=forms.Select(attrs={'class': 'form-control'}),
        #     to_field_name='username',
        #     label='Owner'
        # )

class UpdateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

    def clean_name(self):
        input_name = self.cleaned_data['name']

        names = Category.objects.filter(name__iexact=input_name)
        if names:
            raise ValidationError("Category already exists!")

        return input_name.capitalize()

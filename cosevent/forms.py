from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelChoiceField

from cosevent.models import Event, Category


class DateInput(forms.DateInput):
    input_type = 'date'



class UpdateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'venue', 'category', 'availability', 'artist_name', 'description']

        widgets = {
            'date': DateInput(),
           # 'category': ModelChoiceField(queryset=Category.objects.all())
        }

    def clean_description(self):
        input_description = self.cleaned_data['description']

        if len(input_description) > 400:
            raise ValidationError("Your description text is to long! (max. 400 char)")
        return input_description

    def clean(self):
        try:
            input_date = self.cleaned_data['date']
            input_venue = self.cleaned_data['venue']

            events = Event.objects.filter(date__exact=input_date, venue__iexact=input_venue)
            if events:
                raise ValidationError("Sorry, the venue is booked at this date!")
        except KeyError:
            pass


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

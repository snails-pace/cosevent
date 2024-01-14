from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelChoiceField, DecimalField, widgets

from cosevent.models import Event, Category, User


class DateInput(forms.DateInput):
    # date input class for widgets
    input_type = 'date'

class CustomModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, user):
        return user.username


class UpdateEventForm(forms.ModelForm):
    # Form to update Event
    # Display all fields except id with date as DateInput widget
    class Meta:
        model = Event
        fields = ['name', 'date', 'venue', 'category', 'availability', 'description', 'price']

        widgets = {
            'date': DateInput(),
        }


# Set artist field to readonly
# https://stackoverflow.com/questions/324477/in-a-django-form-how-do-i-make-a-field-readonly-or-disabled-so-that-it-cannot
#     def __init__(self, *args, **kwargs):
#         super(UpdateEventForm, self).__init__(*args, **kwargs)
#         instance = getattr(self, 'instance', None)
#         if instance and instance.pk:
#             self.fields['artist'].required = False
#             self.fields['artist'].widget.attrs['disabled'] = 'disabled'
#
#     def clean_artist(self):
#         instance = getattr(self, 'instance', None)
#         if instance:
#             return instance.artist
#         else:
#             return self.cleaned_data.get('artist', None)


    def clean_description(self):
        # Raises error if description text is longer than 400 chars
        input_description = self.cleaned_data['description']

        if len(input_description) > 400:
            raise ValidationError("Your description text is to long! (max. 400 char)")
        return input_description

    def clean_price(self):
        # Raises error if description text is longer than 400 chars
        input_price = self.cleaned_data['price']

        if input_price < 0:
            raise ValidationError("The price can't be negative")
        return input_price

    def clean(self):
        # Raises error if date and venue are the same (the venue is booked at this date)
        # therefore searches in the database with filter to find matching entries
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
    # Form to update Category
    # Displays name field
    class Meta:
        model = Category
        fields = ['name']

    def clean_name(self):
        # Raises error if the category name exists in the database to avoid duplicates
        # Capitalizes category name
        input_name = self.cleaned_data['name']

        names = Category.objects.filter(name__iexact=input_name)
        if names:
            raise ValidationError("Category already exists!")

        return input_name.capitalize()

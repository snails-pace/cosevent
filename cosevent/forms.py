from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelChoiceField, DecimalField, widgets

from cosevent.models import Event, Category, User, Order


class DateInput(forms.DateInput):
    # date input class for widgets
    input_type = 'date'


class CustomModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, user):
        return user.username


class UpdateEventForm(forms.ModelForm):
    """
    Form to update a specific event
    Displays all fields of the EventModel except id and artist.
    Includes the date field as DateInput widget.
    Inherits from django.forms.ModelForm
    """
    class Meta:
        model = Event
        fields = ['name', 'date', 'venue', 'category', 'availability', 'description', 'price']

        widgets = {
            'date': DateInput(),
            'price': forms.widgets.TextInput()
        }

    def clean_description(self):
        """ Raises an error if the description text is longer than 400 chars
        :param self: UpdateEventForm
        :return: cleaned description
        """
        input_description = self.cleaned_data['description']

        if len(input_description) > 400:
            raise ValidationError("Your description text is to long! (max. 400 char)")
        return input_description

    def clean_price(self):
        """
        Raises an error if a negative price is entered
        :param self: UpdateEventForm
        :return: cleaned price
        """
        input_price = self.cleaned_data['price']

        if input_price < 0:
            raise ValidationError("The price can't be negative")
        return input_price

    def clean(self):
        """
        Raises an error if date and venue are the same (the venue is booked at this date)
        It searches in the database with the filter function to find matching entries.
        :param self: UpdateEventForm
        """
        try:
            input_date = self.cleaned_data['date']
            input_venue = self.cleaned_data['venue']

            events = Event.objects.filter(date__exact=input_date, venue__iexact=input_venue)
            if events:
                raise ValidationError("Sorry, the venue is booked at this date!")
        except KeyError:
            pass


class UpdateCategoryForm(forms.ModelForm):
    """
    Form to create a category
    Inherits from django.forms.ModelForm
    """

    class Meta:
        model = Category
        fields = ['name']

    def clean_name(self):
        """
        Raises an error if the category already exists and capitalizes the category name
        :return: cleaned and capitalized name
        """

        input_name = self.cleaned_data['name']

        names = Category.objects.filter(name__iexact=input_name)
        if names:
            raise ValidationError("Category already exists!")

        return input_name.capitalize()


class OrderForm(forms.ModelForm):
    """
    Form to insert your data to create a Order Model and EventOrder Model
    Displays all fields of the Order Model except id
    Inherits from django.forms.ModelForm
    """
    class Meta:
        model = Order
        fields = ['customer_name', 'customer_email']

    def clean(self):
        pass


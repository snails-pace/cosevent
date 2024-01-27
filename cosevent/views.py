import datetime
import decimal

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView

from cosevent.forms import UpdateEventForm, UpdateCategoryForm, OrderForm
from cosevent.models import Event, Category, Profile, Video, EventOrder


# Create your views here.
class EventListView(generic.ListView):
    model = Event
    context_object_name = 'event_list'
    template_name = 'event_list.html'
    paginate_by = 10


def event_list_view(request):

    # show only future events
    events = Event.objects.filter(date__gte=datetime.date.today())

    paginator = Paginator(events, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'event_list': page_obj, 'my_view': False}
    return render(request, 'event_list.html', context)


@login_required
@require_http_methods(['GET'])
def my_event_list_view(request):
    logged_in_user = request.user
    try:
        profile = Profile.objects.get(user=logged_in_user)
    except Profile.DoesNotExist:
        profile = None
    if profile:
        user_events = Event.objects.filter(artist=profile)
    else:
        user_events = Event.objects.all()

    context = {'event_list': user_events, 'my_view': True}
    return render(request, 'event_list.html', context)


def event_view(request, pk):
    event = get_object_or_404(Event, id=pk)
    context = {'event': event, 'is_owner': False}

    logged_in_user = request.user

    if logged_in_user and not logged_in_user.is_anonymous:
        profile_id = Profile.objects.get(user=logged_in_user).id
        if profile_id == event.artist_id:
            context['is_owner'] = True

    return render(request, 'event.html', context)


@login_required
def event_delete_view(request, pk):
    event = get_object_or_404(Event, id=pk)
    profile_id = Profile.objects.get(user=request.user).id
    # if logged in user is not owner of the event, then raise 403
    if profile_id != event.artist_id:
        raise PermissionDenied("You do not have permission to delete this event")
    if request.method == 'POST':
        event.delete()
        messages.success(request, "Event deleted")
        return redirect('my_events')

    context = {'event': event}
    return render(request, 'event_delete.html', context)


@login_required
def create_event_view(request):
    """Create new events

    GET: Shows a form to enter event data
    POST: Validates the form and saves the new event if valid. Errors will be rendered if not valid
    """
    if request.method == 'POST':
        event_form = UpdateEventForm(request.POST)
        if event_form.is_valid():
            try:
                # set artist field manually to current user
                event_form.instance.artist = Profile.objects.get(user=request.user)
                event_form.save()
                messages.success(request, "Event created")
                return redirect('my_events')
            except Exception as e:
                print(f"Error occurred in {e}")
                return HttpResponse(" An error occurred while creating the Event.")
        else:
            print(event_form.cleaned_data)
            print(event_form.errors)
    else:
        event_form = UpdateEventForm()

    context = {'form': event_form, 'title': 'Create Event'}
    return render(request, 'event_create.html', context)

@login_required
def update_event_view(request, pk):
    """Edit existing event fields like description, name, price"""
    event = get_object_or_404(Event, id=pk)
    profile_id = Profile.objects.get(user=request.user).id
    # if logged in user is not owner of the event, then raise 403
    if profile_id != event.artist_id:
        raise PermissionDenied("You do not have permission to edit this event")
    if request.method == 'POST':
        event_form = UpdateEventForm(request.POST, instance=event)
        if event_form.is_valid():
            event_form.save()
            messages.success(request, "Event updated")
            return redirect('event', pk)
        else:
            messages.error(request, "Form is not valid")
    else:
        event_form = UpdateEventForm(instance=event)

    context = {'form': event_form, 'title': 'Update Event'}
    return render(request, 'event_update.html', context)

@login_required
@require_http_methods(['GET'])
def category_list_view(request):

    categories = Category.objects.all()
    context = {'category_list': categories}

    return render(request, 'category_list.html', context)

@login_required
def create_category_view(request):
    if request.method == 'POST':
        category_form = UpdateCategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            messages.success(request, "Category created")
            return redirect('category_list')
    else:
        category_form = UpdateCategoryForm()

    context = {'form': category_form, 'title': 'Create Category'}
    return render(request, 'category_create.html', context)

@login_required
def category_delete_view(request, pk):
    category = get_object_or_404(Category, id=pk)
    if request.method == 'POST':
        category.delete()
        messages.success(request, "Event deleted")
        return redirect('category_list')

    context = {'category': category}
    return render(request, 'category_delete.html', context)


def cart_view(request):

    tickets = []
    total_price = 0
    if 'cart' in request.session.keys():
        cart = request.session['cart']

        for key, value in cart.items():
            try:
                event = Event.objects.get(id=key)
            except Event.DoesNotExist:
                continue

            sum_price = value['count'] * event.price
            tickets.append({'event_id': event.id, 'name': event.name, 'price': event.price, 'count': value['count'], 'sum': sum_price})
            total_price += sum_price

    context = {'session': request.session, 'tickets': tickets, 'total_price': total_price}

    return render(request, 'cart.html', context)


def cart_update_view(request, pk, increment):
    # increments/decrements the count in the cart item -> increment = increment ('inc') or decrement ('dec')
    pk = str(pk)
    # check if cart exists yet:
    if 'cart' in request.session.keys():
        cart = request.session['cart']
        if increment == 'inc':
            cart[pk]['count'] += 1
        if increment == 'dec':
            cart[pk]['count'] -= 1
            # delete cart item if decreased to 0:
            if cart[pk]['count'] <= 0:
                del cart[pk]

    request.session.modified = True
    return redirect('cart')


def add_to_cart_view(request, pk):
    pk = str(pk)
    if 'cart' not in request.session:
        request.session['cart'] = {}

    if pk not in request.session['cart'].keys():
        request.session['cart'][pk] = {'count': 1}
    else:
        request.session['cart'][pk]['count'] += 1
    # https://docs.djangoproject.com/en/1.11/topics/http/sessions/#when-sessions-are-saved
    request.session.modified = True
    return redirect('cart')

def buy_view(request):
    """Buy tickets

    POST: Validates the form and saves the new order if valid. Errors will be rendered if not valid
    """

    # Show tickets as in cart_view therefore add also list of tickets, where ticket is dict entry with count value from session
    tickets = []
    total_price = decimal.Decimal(0)
    if 'cart' in request.session.keys():
        cart = request.session['cart']

        for key, value in cart.items():
            try:
                event = Event.objects.get(id=key)
            except Event.DoesNotExist:
                continue

            sum_price = value['count'] * event.price
            tickets.append({'event': event, 'name': event.name, 'price': event.price, 'count': value['count'],
                            'sum': sum_price})
            total_price += sum_price

    # if POST set total price and save Order model
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            try:
                # set artist field manually to current user
                order_form.instance.total_price = total_price
                order = order_form.save()
                #print(order)
                #messages.success(request, "Event created")

                # Create an EventOrder model for each Event - Order relationship
                for ticket in tickets:
                    print(ticket)
                    EventOrder.objects.create(event=ticket['event'], ticket_count=ticket['count'], price=ticket['sum'], order=order)
                #
                del request.session['cart']
                request.session['order_nr'] = order.id
                return redirect('purchased')
            except Exception as e:
                print(f"Error occurred in {e}")
                return HttpResponse(" An error occurred while submitting the order.")
        else:
            print(order_form.cleaned_data)
            print(order_form.errors)
    else:
        order_form = OrderForm()

    context = {'form': order_form, 'title': 'Buy Tickets', 'session': request.session, 'tickets': tickets, 'total_price': total_price}
    return render(request, 'buy.html', context)


def purchased_view(request):
    order = request.session['order_nr']
    context = {'order': order}
    return render(request, 'purchased.html', context)
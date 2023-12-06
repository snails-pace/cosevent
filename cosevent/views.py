from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView

from cosevent.forms import UpdateEventForm, UpdateCategoryForm
from cosevent.models import Event, Category, Profile


# Create your views here.
class EventListView(generic.ListView):
    model = Event
    context_object_name = 'event_list'
    template_name = 'event_list.html'


def event_list_view(request):

    events = Event.objects.all()
    context = {'event_list': events, 'my_view': False}
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
        user_events = Event.objects.filter(owner=profile)
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
        if profile_id == event.owner_id:
            context['is_owner'] = True

    return render(request, 'event.html', context)


# class UpdateEventView(SuccessMessageMixin, generic.UpdateView):
#     model = Event
#     form_class = UpdateEventForm
#     template_name = 'event_update.html'
#     success_message = 'Your event %(name)s was saved'
#
#     def get_success_url(self):
#         return reverse_lazy('event', args=[self.object.pk])
#
#     def form_valid(self, form):
#         submitted_date = form.cleaned_data
#
#         return super().form_valid(form)



# class CreateEventView(SuccessMessageMixin, generic.CreateView):
#     model = Event
#     form_class = UpdateEventForm
#     template_name = 'event_create.html'
#     success_message = 'Your event %(name)s was saved'
#
#     def get_success_url(self):
#         return reverse_lazy('event', args=[self.object.pk])
#
#     def form_valid(self, form):
#         submitted_date = form.cleaned_data
#
#         return super().form_valid(form)



@login_required
def event_delete_view(request, pk):
    event = get_object_or_404(Event, id=pk)
    profile_id = Profile.objects.get(user=request.user).id
    # if logged in user is not owner of the event, then raise 403
    if profile_id != event.owner_id:
        raise PermissionDenied("You do not have permission to delete this event")
    if request.method == 'POST':
        event.delete()
        messages.success(request, "Event deleted")
        return redirect('my_events')

    context = {'event': event}
    return render(request, 'event_delete.html', context)


@login_required
def create_event_view(request):
    if request.method == 'POST':
        event_form = UpdateEventForm(request.POST)
        if event_form.is_valid():
            try:
                event_form.save()
                return redirect('event_list')
            except Exception as e:
                print(f"Error occurred in {e}")
                return HttpResponse(" An error occurred while creating the Event.")
        else:
            print(event_form.cleaned_data)
            print(event_form.errors)
        return redirect('my_events')
    else:
        profile_id = Profile.objects.get(user=request.user).id
        event_form = UpdateEventForm(initial={'owner': profile_id})

    context = {'form': event_form}
    context['title'] = 'Create Event'
    return render(request, 'event_create.html', context)

@login_required
def update_event_view(request, pk):
    event = get_object_or_404(Event, id=pk)
    profile_id = Profile.objects.get(user=request.user).id
    # if logged in user is not owner of the event, then raise 403
    if profile_id != event.owner_id:
        raise PermissionDenied("You do not have permission to edit this event")
    if request.method == 'POST':
        event_form = UpdateEventForm(request.POST, instance=event)
        if event_form.is_valid():
            event_form.save()
        else:
            pass

        return redirect('my_events', pk)
    else:

        event_form = UpdateEventForm(instance=event)

        context = {'form': event_form}
        context['title'] = 'Update Event'
        return render(request, 'event_update.html', context)


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

    cart = request.session['cart']
    tickets = []
    total_price = 0
    for key, value in cart.items():
        event = Event.objects.get(id=key)
        sum_price = value['count'] * event.price
        tickets.append({'event_id': event.id, 'name': event.name, 'price': event.price, 'count': value['count'], 'sum': sum_price})
        total_price += sum_price

    context = {'session': request.session, 'tickets': tickets, 'total_price': total_price}

    return render(request, 'cart.html', context)


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

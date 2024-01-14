from datetime import datetime, date

from django.test import TestCase, Client
from django.urls import reverse

from cosevent.models import User, Profile, Category, Event


# Create your tests here.

class UserProfileTestCase(TestCase):
    def setUp(self):

        # Creation of a sample user
        self.user = User.objects.create_user(
            username='test@example.net'
        )

        self.profile = Profile.objects.create(
            user=self.user,
            nickname='Pikachu',
            birthdate=datetime.now().date()
        )

    def test_user_profile_creation(self):
        self.assertEqual(self.user.username, 'test@example.net')
        self.assertEqual(self.profile.user, self.user)
        self.assertEqual(self.profile.nickname, 'Pikachu')

    def test_user_str_method(self):
        self.assertEqual(str(self.user), 'test@example.net')

    def test_profile_str_method(self):
        self.assertEqual(str(self.profile), 'Pikachu')

    def test_profile_with_non_existing_user(self):
        with self.assertRaises(Exception):
            Profile.objects.create(
                user=6,
                nickname='Igel',
                birthdate=datetime.now().date()
            )


class CategoryTestCase(TestCase):
    def setUp(self):

        # Creation of a sample user
        self.user = User.objects.create_user(
            username='test@example.net'
        )

        self.profile = Profile.objects.create(
            user=self.user,
            nickname='Pikachu',
            birthdate=datetime.now().date()
        )

        self.category = Category.objects.create(
            name='fun'
        )

    def test_category_profile_creation(self):
        self.assertNotEqual(self.category.name, 'Fun')
        self.assertEqual(self.category.name, 'fun')


class EventTestCase(TestCase):
    def setUp(self):

        # Creation of a sample user
        self.user = User.objects.create_user(
            username='test@example.net',
            password='testPassword12'
        )

        self.profile = Profile.objects.create(
            user=self.user,
            nickname='Pikachu',
            birthdate=datetime.now().date()
        )

        self.category = Category.objects.create(
            name='Fun'
        )

        self.event = Event.objects.create(
            name='Blumen pflanzen',
            date=datetime.now().date(),
            description='bla',
            venue='Woanders',
            category=self.category,
            availability=1,
            price=4.20,
            artist=self.profile
        )

    def test_event_creation(self):
        self.assertIsNotNone(self.event.name)
        self.assertEqual(self.event.name, 'Blumen pflanzen')
        self.assertEqual(self.event.description, 'bla')
        self.assertEqual(self.event.venue, 'Woanders')
        self.assertEqual(self.event.category.name, 'Fun')
        self.assertEqual(self.event.availability, 1)
        self.assertEqual(self.event.price, 4.20)
        self.assertEqual(self.event.artist, self.profile)
        self.assertNotEqual(self.event.category.name, 'fun')
        self.assertIsInstance(self.profile.birthdate, date)


    def test_event_creation_with_non_existing_artist(self):
        with self.assertRaises(Exception):
            Event.objects.create(
                name='Bird watching',
                date=datetime.now().date(),
                description='bla',
                venue='Woanders',
                category=self.category,
                availability=1,
                price=4.20,
                artist=4
            )

    def test_event_creation_with_non_existing_category(self):
        with self.assertRaises(Exception):
            Event.objects.create(
                name='Bird watching',
                date=datetime.now().date(),
                description='bla',
                venue='Woanders',
                category=8,
                availability=1,
                price=4.20,
                artist=self.profile
            )

    def test_event_creation_with_missing_inputs(self):
        with self.assertRaises(Exception):
            Event.objects.create(
                name=None,
                date=datetime.now().date(),
                description='bla',
                venue='Woanders',
                category=self.category,
                availability=1,
                price=4.20,
                artist=self.profile
            )


class UpdateEventViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='test@example.net',
            email='test@example.net',
            password='testPassword'
        )

        self.profile = Profile.objects.create(
            user=self.user,
            nickname='Pikachu',
            birthdate=datetime.now().date()
        )

        self.category = Category.objects.create(
            name='Fun'
        )

        self.event = Event.objects.create(
            name='Blumen pflanzen',
            date=datetime.now().date(),
            description='bla',
            venue='Woanders',
            category=self.category,
            availability=1,
            price=4.20,
            artist=self.profile
        )

        self.client = Client()

    def test_get_update_unauthenticated(self):
        """GET request to the view without being logged in"""
        response = self.client.get(reverse('event_update', args=[self.event.pk]))

        self.assertEqual(response.status_code, 302)
        # Check redirect to login page
        expected_redirect_url = reverse('login') + '?next=' + reverse('event_update', args=[self.event.pk])
        self.assertRedirects(response, expected_redirect_url)

    def test_post_update_unauthenticated(self):
        """POST request to the view without being logged in"""
        response = self.client.post(reverse('event_update', args=[self.event.pk]))

        self.assertEqual(response.status_code, 302)
        # Check redirect to login page
        expected_redirect_url = reverse('login') + '?next=' + reverse('event_update', args=[self.event.pk])
        self.assertRedirects(response, expected_redirect_url)

    def test_get_update_authenticated(self):
        """GET request to the view authenticated"""
        result = self.client.force_login(self.user)

        response = self.client.get(reverse('event_update', args=[self.event.pk]))

        self.assertEqual(response.status_code, 200)
        self.assertTrue('title' in response.context)

        self.assertContains(response, 'Blumen pflanzen')
        self.assertContains(response, 'bla')
        self.assertContains(response, 'Woanders')
        self.assertContains(response, self.profile)

    def test_post_update_authenticated(self):
        """GET request to the view authenticated"""
        self.client.force_login(self.user)

        response = self.client.post(reverse('event_update', args=[self.event.pk]), {
            'name': 'Bird watching',
            'date': datetime.now().date(),
            'description': 'bla',
            'venue': 'Draussen',
            'category': self.category.pk,
            'availability': 1,
            'price': 4.20,
            'artist': self.profile.pk})

        self.assertEqual(response.status_code, 302)
        self.event.refresh_from_db()

        self.assertEqual('Bird watching', self.event.name)
        self.assertEqual('Draussen', self.event.venue)

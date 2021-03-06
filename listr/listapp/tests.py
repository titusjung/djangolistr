from django.test import TestCase
from .models import Entry
from django.contrib.auth import get_user_model
# Create your tests here.
class EntryModelTest(TestCase):

    def test_string_representation(self):
        entry = Entry(title="My entry title")
        self.assertEqual(str(entry),entry.title)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Entry._meta.verbose_name_plural),"entries")

    def test_get_absolute_url(self):
        user = get_user_model().objects.create(username='some_user')
        entry = Entry.objects.create(title="My entry title", author=user)
        self.assertIsNotNone(entry.get_absolute_url())

class ProjectTests(TestCase):

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

class HomePageTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(username='some_user')

    def test_one_entry(self):
        Entry.objects.create(title='1-title',description='1-description',author=self.user)
        response = self.client.get('/')
        self.assertContains(response,'1-title')
        self.assertContains(response,'1-description')

    def test_two_entries(self):
        Entry.objects.create(title='1-title',description='1-description',author=self.user)
        Entry.objects.create(title='2-title',description='2-description',author=self.user)
        response = self.client.get('/')
        self.assertContains(response,'1-title')
        self.assertContains(response,'1-description')
        self.assertContains(response,'2-title')

    def test_no_entries(self):
        response = self.client.get('/')
        self.assertContains(response, 'No entries')

class EntryViewTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(username='some_user')
        self.entry = Entry.objects.create(title='1-title', description='1-description',
                                          author=self.user)

    def test_basic_view(self):
        response = self.client.get(self.entry.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_title_in_entry(self):
        response = self.client.get(self.entry.get_absolute_url())
        self.assertContains(response, self.entry.title)

    def test_body_in_entry(self):
        response = self.client.get(self.entry.get_absolute_url())
        self.assertContains(response, self.entry.description)

class LoginViewTest(TestCase):

    def test_login_page(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_login_page_content(self):
        response = self.client.get('/login/')
        self.assertContains(response, 'Email')
        self.assertContains(response, 'Password')
        
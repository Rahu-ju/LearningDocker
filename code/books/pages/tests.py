from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView



class HomePageTest(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)


    def test_home_page_template_name(self):
        self.assertTemplateUsed(self.response, 'home.html')


    def test_home_page_contains_correct_html(self):
        self.assertContains(self.response, 'Home page.')
        self.assertNotContains(self.response, 'I am rahu.')


    def test_home_page_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'I am rahu.')


    def test_homepage_url_resolves_HomePageView(self):
        view = resolve('/')
        self.assertEqual( view.func.__name__, HomePageView.as_view().__name__ )
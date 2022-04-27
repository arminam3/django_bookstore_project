from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse

class HomePageTest(TestCase):
    # def setUpTestData(cls):
    #     cls.user = User.objects.create(username='ahmad',password=3920906969)

    def test_home_page_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Hello')
    def test_home_page_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'pages/home.html')


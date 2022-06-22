from django.test import TestCase
from django.urls import reverse
from django.urls import resolve
from django.contrib import admin
from newsfeed.models import Artwork, CodeProject


# Create automated tests here.
# to test your tests:
# "python manage.py test"

class URLTests(TestCase):

    def setUp(self):
        self.test_object = Artwork.objects.create(title="Test Title")

    # Check if the about-me page works and returns 200.
    def test_test_about_me(self):
        response = self.client.get(reverse('about_me'))
        self.assertEqual(response.status_code, 200)

    # Test contact page basic load.
    def test_test_contact(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
    
    # Test homepage
    def test_test_homepage(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


    # Test single artwork view
    #def test_test_single_artwork(self):
    #    url = reverse('art_view', args=[1])
    #    self.assertEqual(url, '/1/single-artwork/')

    def test_test_single_artwork_view(self):
        url = reverse('art_view', args=[1])
        self.assertEqual(resolve(url).view_name, 'art_view')

    def test_test_single_artwork_url_render(self):
        response = self.client.get(reverse('art_view', kwargs={'id' : self.test_object.id}))
        self.assertEqual(response.status_code, 200)


    # Test single code project view
    def test_test_single_code_view(self):
        url = reverse('code_view', args=[1])
        self.assertEqual(resolve(url).view_name, 'code_view')

    # def test_test_admin_url(self):
    #    url = reverse('admin')
    #    self.assertEqual(resolve(url).view_name, 'admin')
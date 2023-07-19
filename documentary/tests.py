from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Documentary

class DocumentaryTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.documentary = Documentary.objects.create(
            title='Test Documentary',
            description='This is a test documentary',
            year=2022,
            author='Test Author',
        )

    def test_documentary_list_view(self):
        url = reverse('documentary_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'documentary/documentary_list.html')

    def test_documentary_list_ajax_view(self):
        url = reverse('documentary_list')
        data = {'q': 'Test'}
        response = self.client.get(url, data, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'documentary/documentary_list_ajax.html')

    def test_documentary_details_view(self):
        url = reverse('documentary_details', args=[self.documentary.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'documentary/documentary_details.html')

    def test_register_documentary_view(self):
        url = reverse('register_documentary')
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'documentary/register_documentary.html')

    def test_documentary_registered_view(self):
        url = reverse('documentary_registered')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'documentary/documentary_registered.html')

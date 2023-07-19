from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserProfile

class AuthenticationTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.user_profile = UserProfile.objects.create(user=self.user, bio='Test bio')

    def test_user_profile_creation(self):
        self.assertEqual(str(self.user_profile), self.user.username)

    def test_user_login_view(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/login.html')

    def test_user_signup_view(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/signup.html')

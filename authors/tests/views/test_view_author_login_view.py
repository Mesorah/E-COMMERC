from django.test import TestCase
from django.contrib.auth.models import User
from authors.models import UserProfile
from django.urls import reverse


class TestAuthorLoginView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='Test',
            password='Test'
        )

        self.profile = UserProfile.objects.create(
            user=self.user,
            cpf='04887398026'
        )

        return super().setUp()

    def test_if_the_correct_login_is_redirected(self):
        data = {
            'username': 'Test',
            'password': 'Test'
        }

        response = self.client.post(reverse('authors:login'), data=data)

        self.assertEqual(response.status_code, 302)

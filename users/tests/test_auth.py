from .factories import UserFactory
from django.test import TestCase


class TestAuth(TestCase):
    def test_login(self):
        self.user = UserFactory.with_password("secret123")

        resp = self.client.post(
            "/api/v1/auth/login/",
            {"email": self.user.email, "password": "secret123"},
            content_type="application/json",
        )

        self.assertEqual(resp.status_code, 200)
        self.assertTrue("key" in resp.json())

    def test_signup_not_allowed(self):
        resp = self.client.post(
            "/api/v1/auth/register/",
            {
                "email": "test@example.com",
                "password1": "S3cr3t?N0tR34lly",
                "password2": "S3cr3t?N0tR34lly",
            },
            content_type="application/json",
        )

        self.assertEqual(resp.status_code, 404)

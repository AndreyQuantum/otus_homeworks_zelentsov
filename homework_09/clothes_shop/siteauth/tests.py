

from siteauth.models import UserModel

from django.contrib.auth.models import AbstractUser
from django.test import TestCase
from django.urls import reverse

from django.utils.translation import gettext_lazy as _
from siteauth.models import UserModel
from siteauth.forms import UserCreationForm


class UserRegisterTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user_reg_data = {
            "username": "user_test",
            "email": "john@example.com",
            "password1": "te125te06",
            "password2": "te125te06",
        }

        cls.user_reg_data_invalid_pass = {
            "username": "john",
            "email": "john@example.com",
            "password1": "235325terwe",
            "password2": "terwe12132",
        }

    def test_user_register_success(self):
        response = self.client.post(
            reverse("siteauth:register"),
            data=self.user_reg_data,
        )
        self.assertURLEqual(response.url, reverse("shopapp:list"))
        self.assertEqual(response.status_code, 302)

        user: AbstractUser = UserModel.objects.get(username=self.user_reg_data["username"])
        self.assertEqual(user.email, self.user_reg_data["email"])

    # def test_user_register_username_exists_error(self):
    #     response = self.client.post(
    #         reverse("siteauth:register"),
    #         data=self.user_reg_data,
    #     )
    #     self.assertEqual(response.status_code, 302)
    #
    #     response = self.client.post(
    #         reverse("siteauth:register"),
    #         data=self.user_reg_data,
    #     )
    #     self.assertEqual(response.status_code, 200)
    #     print(response)
    #     self.assertFormError(
    #         response,
    #         "form",
    #         "username",
    #         _("A user with that username already exists."),
    #     )
    #
    # def test_user_register_password_doesnt_match(self):
    #     response = self.client.post(
    #         reverse("siteauth:register"),
    #         data=self.user_reg_data_invalid_pass,
    #     )
    #     self.assertEqual(response.status_code, 200)
    #     self.assertFormError(
    #         response,
    #         "form",
    #         "password2",
    #         UserCreationForm.error_messages["password_mismatch"],
    #     )


class UserLoginTestCase(TestCase):

    def setUp(self) -> None:
        password = "test_password"
        self.user: AbstractUser = UserModel.objects.create_user(
            "test_user",
            "test_user@example.com",
            password,
        )
        self.password = password

    def test_user_login(self):
        response = self.client.post(
            reverse("siteauth:login"),
            data={
                "username": self.user.username,
                "password": self.password,
            },
        )

        self.assertEqual(response.url, reverse("shopapp:list"))

        response = self.client.get(reverse("shopapp:list"))
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context["user"].is_anonymous)

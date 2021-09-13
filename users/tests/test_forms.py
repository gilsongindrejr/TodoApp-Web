from django.test import TestCase

from users.forms import CustomUserCreationForm, CustomUserChangeForm


class CreationFormTestCase(TestCase):

    def setUp(self):
        self.data = {
            'email': 'user@email.com',
            'password1': '4231django',
            'password2': '4231django',
            'first_name': 'First',
            'last_name': 'Last',
        }

    def test_creation_form(self):
        form = CustomUserCreationForm(data=self.data)
        self.assertTrue(form.save())

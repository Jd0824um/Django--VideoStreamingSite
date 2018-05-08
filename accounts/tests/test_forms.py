
from django.test import TestCase

from django.contrib.auth.models import User
from admin.forms import RegistrationForm, EditProfileForm
import string


class RegistrationFormTests(TestCase):

    def test_register_user_with_valid_data_is_valid(self):
        form_data = { 'username' : 'bob' , 'email' : 'bob@bob.com', 'first_name' : 'bob',
         'last_name' : 'whatever', 'password1' : 'qwertyuiop', 'password2' : 'qwertyuiop' }
        form = rRegistrationForm(form_data)
        self.assertTrue(form.is_valid())

    def test_register_user_with_missing_data_fails(self):
        form_data = { 'username': 'bob', 'email' : 'bob@bob.com', 'first_name' : 'bob', 'last_name' : 'whatever', 'password1' : 'qwertyuiop', 'password2' : 'qwertyuiop' }
        for field in form_data.keys():
            data = dict(form_data)
            del(data[field])
            form = RegistrationForm(data)
            self.assertFalse(form.is_valid())


    def test_register_user_with_password_mismatch_fails(self):
        form_data = { 'username' : 'another_bob' , 'email' : 'bob@bob.com', 'first_name' : 'bob', 'last_name' : 'whatever', 'password1' : 'qwertyuiop', 'password2' : 'qwertyuiop2' }
        form = RegistrationForm(form_data)
        self.assertFalse(form.is_valid())


    def test_register_user_with_email_already_in_db_fails(self):
        bob = User(username='bob', email='bob@bob.com', first_name='bob', last_name='bob')
        bob.save()

        form_data = { 'username' : 'another_bob' , 'email' : 'bob@bob.com', 'first_name' : 'bob', 'last_name' : 'whatever', 'password1' : 'qwertyuiop', 'password2' : 'qwertyuiop' }
        form = RegistrationForm(form_data)
        self.assertFalse(form.is_valid())


    def test_register_user_with_username_already_in_db_fails(self):
        bob = User(username='bob', email='bob@bob.com')
        bob.save()

        form_data = { 'username' : 'bob' , 'email' : 'another_bob@bob.com', 'first_name' : 'bob', 'last_name' : 'whatever', 'password1' : 'qwertyuiop', 'password2' : 'qwertyuiop' }
        form = RegistrationForm(form_data)
        self.assertFalse(form.is_valid())

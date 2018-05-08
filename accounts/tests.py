from django.test import TestCase
accounts.models import UserProfile
from localflavor.us.models import USStateField


class UserProfileTestCase(TestCase):
    def setup(self):
        user_profile = UserProfile.objects.create(description='Test', city='Minneapolis', phone='7777777777')

    def test_user_profile_description(self):
        self.assertEqual(user_profile.description, 'Test')

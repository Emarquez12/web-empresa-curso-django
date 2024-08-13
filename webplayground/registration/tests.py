from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.

class ProfileTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('test1', 'test1@test1.com','test124578@')
    
    def test_profile_exists(self):
        exists = Profile.objects.filter(user__username='test1').exists()
        self.assertEqual(exists, True)

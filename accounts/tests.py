from django.test import TestCase

from django.contrib.auth import get_user_model

# Create your tests here.



class django_custom_test(TestCase):

    def setUp(self):


        self.user = get_user_model().objects.create_user(
            username = 'hadi',
            email = 'hadi19932@gmail.com',
            password = 'hadi12345'
        )

    def test_create_new_user(self):

        self.assertEquals(self.user.email,'hadi19932@gmail.com')
        self.assertEquals(self.user.username,'hadi')
        

    def test_duplicate_emails(self):
            pass
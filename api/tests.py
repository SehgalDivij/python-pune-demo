from django.test import TestCase

# Create your tests here.

from rest_framework.test import APITestCase
from django.core.urlresolvers import reverse
from rest_framework import status

class IdentityTest(APITestCase):
    def test_whoami(self):
        """
        Check if I am identified right..
        """
        url = reverse('identify_me')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'name': 'Divij Sehgal', 'occupation': 'Programming', 'reason': 'It\'s fun', 'age':22})

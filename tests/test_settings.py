import unittest
import os

from pyjss.settings import Credentials, set_credentials, get_credentials, create_auth_file, get_auth_from_file


class TestSettingsCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_set_credentials(self):
        pass

    def test_get_credentials(self):
        pass

    def test_create_auth_file(self):
        pass

    def test_get_auth_from_file(self):
        credentials_file = os.path.join(
            os.path.dirname(__file__), 'credentials.json')
        get_auth_from_file(credentials_file)
        self.assertEqual(Credentials.get(), 'url_value')

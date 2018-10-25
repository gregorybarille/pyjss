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
        credentials_file = os.path.join(os.path.dirname(__file__), 'good_credentials_file.json')
        get_auth_from_file(credentials_file)
        self.assertEqual(Credentials.url, 'url_value')
        self.assertEqual(Credentials.username, 'username_value')
        self.assertEqual(Credentials.password, 'password_value')
        with self.assertRaises(KeyError):
            bad_credentials_file = os.path.join(os.path.dirname(__file__), 'bad_credentials_file.json')
            get_auth_from_file(bad_credentials_file)
        with self.assertRaises(OSError):
            not_credentials_file = os.path.join(os.path.dirname(__file__), 'not_credentials_file.json')
            get_auth_from_file(not_credentials_file)

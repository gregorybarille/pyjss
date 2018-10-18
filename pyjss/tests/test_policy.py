import unittest

import sys
sys.path.append('..')
from ..objects_list import Policy
from ..templates import default_policy_template
from bs4 import BeautifulSoup as soup


class PolicyTestCase(unittest.TestCase):
    policy_object = Policy(soup(default_policy_template, 'xml'))

    def setUp(self):
        pass

    def test_Policy_attribute_id(self):
        self.policy_object.id = 2
        self.assertEqual(self.policy_object.id, '2', 'Policy.id - FAILED')

    def test_Policy_attribute_name(self):
        self.policy_object.name = 'test_name'
        self.assertEqual(self.policy_object.name, 'test_name', 'Policy.name - FAILED')

    def test_Policy_attribute_enabled(self):
        self.policy_object.enabled = 'true'
        self.assertEqual(self.policy_object.enabled, 'true', 'Policy.enabled - FAILED')

    def test_Policy_attribute_site(self):
        self.policy_object.site = 'Random_site'
        self.assertIn('Random_site', str(self.policy_object.site),
                      'Policy.site - FAILED')

    def test_Policy_attribute_category(self):
        self.policy_object.category = 'Random_category'
        self.assertIn('Random_category', str(self.policy_object.category), 'Policy.category - FAILED')

    def test_Policy_attribute_trigger_checkin(self):
        self.policy_object.trigger_checkin = 'true'
        self.assertEqual(self.policy_object.trigger_checkin, 'true', 'Policy.trigger_checkin - FAILED')
        with self.assertRaises(ValueError):
            self.policy_object.trigger_checkin = 'RandomValue'

    def test_Policy_attribute_trigger_enrollment_complete(self):
        self.policy_object.trigger_enrollment_complete = 'true'
        self.assertEqual(self.policy_object.trigger_enrollment_complete, 'true', 'Policy.trigger_enrollment_complete - FAILED')
        with self.assertRaises(ValueError):
            self.policy_object.trigger_enrollment_complete = 'RandomValue'

    def test_Policy_attribute_trigger_login(self):
        self.policy_object.trigger_login = 'true'
        self.assertEqual(self.policy_object.trigger_login, 'true', 'Policy.trigger_login - FAILED')
        with self.assertRaises(ValueError):
            self.policy_object.trigger_login = 'RandomValue'

    def test_Policy_attribute_trigger_logout(self):
        self.policy_object.trigger_logout = 'true'
        self.assertEqual(self.policy_object.trigger_logout, 'true', 'Policy.trigger_logout - FAILED')
        with self.assertRaises(ValueError):
            self.policy_object.trigger_logout = 'RandomValue'

    def test_Policy_attribute_trigger_network_state_changed(self):
        self.policy_object.trigger_network_state_changed = 'true'
        self.assertEqual(self.policy_object.trigger_network_state_changed, 'true', 'Policy.trigger_network_state_changed - FAILED')
        with self.assertRaises(ValueError):
            self.policy_object.trigger_network_state_changed = 'RandomValue'

    def test_Policy_attribute_trigger_startup(self):
        self.policy_object.trigger_startup = 'true'
        self.assertEqual(self.policy_object.trigger_startup, 'true', 'Policy.trigger_startup - FAILED')
        with self.assertRaises(ValueError):
            self.policy_object.trigger_startup = 'RandomValue'

    def test_Policy_attribute_trigger_other(self):
        self.policy_object.trigger_other = 'RandomValue'
        self.assertEqual(self.policy_object.trigger_other, 'RandomValue', 'Policy.trigger_other - FAILED')

    def test_Policy_attribute_offline(self):
        self.policy_object.offline = 'true'
        self.assertEqual(self.policy_object.offline, 'true', 'Policy.trigger_other - FAILED')
        with self.assertRaises(ValueError):
            self.policy_object.offline = 'RandomValue'

    def test_Policy_attribute_frequency(self):
        self.policy_object.frequency = 'Once per user'
        self.assertEqual(self.policy_object.frequency, 'Once per user', 'Policy.frequency - FAILED')

    def test_Policy_attribute_target_drive(self):
        self.policy_object.target_drive = '/Drive'
        self.assertEqual(self.policy_object.target_drive, '/Drive', 'Policy.target_drive - FAILED')

    def test_Policy_attribute_update_inventory(self):
        self.policy_object.update_inventory = 'true'
        self.assertEqual(self.policy_object.update_inventory, 'true', 'Policy.update_inventory - FAILED')
        with self.assertRaises(ValueError):
            self.policy_object.update_inventory = 'RandomValue'

    def test_Policy_attribute_reset_computer_name(self):
        self.policy_object.reset_computer_name = 'true'
        self.assertEqual(self.policy_object.reset_computer_name, 'true', 'Policy.reset_computer_name - FAILED')
        with self.assertRaises(ValueError):
            self.policy_object.reset_computer_name = 'RandomValue'

    def test_Policy_attribute_install_cached_packages(self):
        self.policy_object.install_cached_packages = 'true'
        self.assertEqual(self.policy_object.install_cached_packages, 'true', 'Policy.install_cached_packages - FAILED')
        with self.assertRaises(ValueError):
            self.policy_object.install_cached_packages = 'RandomValue'

    def test_Policy_attribute_fix_permissions(self):
        self.policy_object.fix_permissions = 'true'
        self.assertEqual(self.policy_object.fix_permissions, 'true', 'Policy.fix_permissions - FAILED')
        with self.assertRaises(ValueError):
            self.policy_object.fix_permissions = 'RandomValue'

    def test_Policy_attribute_fix_by_host(self):
        self.policy_object.fix_by_host = 'true'
        self.assertEqual(self.policy_object.fix_by_host, 'true', 'Policy.fix_by_host - FAILED')
        with self.assertRaises(ValueError):
            self.policy_object.fix_by_host = 'RandomValue'

    def test_Policy_attribute_fix_system_caches(self):
        self.policy_object.fix_system_caches = 'true'
        self.assertEqual(self.policy_object.fix_system_caches, 'true', 'Policy.fix_system_caches - FAILED')
        with self.assertRaises(ValueError):
            self.policy_object.fix_system_caches = 'RandomValue'

    def test_Policy_attribute_fix_user_caches(self):
        self.policy_object.fix_user_caches = 'true'
        self.assertEqual(self.policy_object.fix_user_caches, 'true', 'Policy.fix_user_caches - FAILED')
        with self.assertRaises(ValueError):
            self.policy_object.fix_user_caches = 'RandomValue'

    def test_Policy_attribute_verify_disk(self):
        self.policy_object.verify_disk = 'true'
        self.assertEqual(self.policy_object.verify_disk, 'true', 'Policy.verify_disk - FAILED')
        with self.assertRaises(ValueError):
            self.policy_object.verify_disk = 'RandomValue'

    def test_Policy_attribute_search_by_path(self):
        self.policy_object.search_by_path = '/Path/'
        self.assertEqual(self.policy_object.search_by_path, '/Path/', 'Policy.search_by_path - FAILED')

    def test_Policy_attribute_delete_file(self):
        self.policy_object.delete_file = 'true'
        self.assertEqual(self.policy_object.delete_file, 'true', 'Policy.delete_file - FAILED')
        with self.assertRaises(ValueError):
            self.policy_object.delete_file = 'RandomValue'

    def test_Policy_attribute_search_by_filename(self):
        self.policy_object.search_by_filename = 'filename'
        self.assertEqual(self.policy_object.search_by_filename, 'filename', 'Policy.search_by_filename - FAILED')

    def test_Policy_attribute_update_locate_database(self):
        self.policy_object.update_locate_database = 'true'
        self.assertEqual(self.policy_object.update_locate_database, 'true', 'Policy.locate_database - FAILED')
        with self.assertRaises(ValueError):
            self.policy_object.update_locate_database = 'RandomValue'

    def test_Policy_attribute_search_spotlight(self):
        self.policy_object.search_spotlight = 'filename'
        self.assertEqual(self.policy_object.search_spotlight, 'filename', 'Policy.search_spotlight - FAILED')

    def test_Policy_attribute_search_process(self):
        self.policy_object.search_process = 'process'
        self.assertEqual(self.policy_object.search_process, 'process', 'Policy.search_process - FAILED')

    def test_Policy_attribute_kill_process(self):
        self.policy_object.kill_process = 'true'
        self.assertEqual(self.policy_object.kill_process, 'true', 'Policy.kill_process - FAILED')
        with self.assertRaises(ValueError):
            self.policy_object.kill_process = 'RandomValue'

    def test_Policy_attribute_run_command(self):
        self.policy_object.run_command = 'command'
        self.assertEqual(self.policy_object.run_command, 'command', 'Policy.run_command - FAILED')

    def test_Policy_function_create_tag(self):
        id_tag = self.policy_object._create_tag('tag', 134)
        self.assertEqual(str(id_tag), '<tag><id>134</id></tag>')
        name_tag = self.policy_object._create_tag('tag', 'random_name')
        self.assertEqual(str(name_tag), '<tag><name>random_name</name></tag>')

    def test_Policy_function_create_secondary_tag(self):
        id_tag = self.policy_object._create_secondary_tag('main_tag', 'secondary_tag', 'secondary_tag_value', 134)
        self.assertEqual(str(id_tag), '<main_tag><id>134</id><secondary_tag>secondary_tag_value</secondary_tag></main_tag>')
        name_tag = self.policy_object._create_secondary_tag('main_tag', 'secondary_tag', 'secondary_tag_value', 'main_tag_value')
        self.assertEqual(str(name_tag), '<main_tag><name>main_tag_value</name><secondary_tag>secondary_tag_value</secondary_tag></main_tag>')


if __name__ == '__main__':
    unittest.main()

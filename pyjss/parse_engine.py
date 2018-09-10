from bs4 import BeautifulSoup as soup
import inspect

def clear_scope(policy_data):
	new_data = soup(policy_data, 'xml')

class Policy:

	def __init__(self, xml_data ):
		xml_data = soup(xml_data, 'xml')
		self.data = xml_data
		self.id = xml_data.policy.general.find('id')
		self.name = xml_data.policy.general.find('name')
		self.category = xml_data.policy.general.find('category')
		self.scope = xml_data.policy.find('scope')
		self.allcomputers = xml_data.policy.scope.find('all_computers')
		self.computers = xml_data.policy.scope.find('computers')
		self.computergroups = xml_data.policy.scope.find('computer_groups')
		self.buildings = xml_data.policy.scope.find('buildings')
		self.departments = xml_data.policy.scope.find('departments')
		self.limitations = xml_data.policy.scope.find('limitations')
		self.limitations_users = xml_data.policy.scope.limitations.find('users')
		self.limitations_usergroups = xml_data.policy.scope.limitations.find('user_groups')
		self.limitations.networksegments = xml_data.policy.scope.limitations.find('network_segments')
		self.limitations.ibeacons = xml_data.policy.scope.limitations.find('ibeacons')
		self.exclusions = xml_data.policy.scope.exclusions
		self.exclusions.computers = xml_data.policy.scope.exclusions.computers
		self.exclusions.computergroups = xml_data.policy.scope.exclusions.computer_groups
		self.exclusions.buildings = xml_data.policy.scope.exclusions.buildings
		self.exclusions.departments = xml_data.policy.scope.exclusions.departments
		self.exclusions.users = xml_data.policy.scope.exclusions.users
		self.exclusions.user_groups = xml_data.policy.scope.exclusions.user_groups
		self.exclusions.network_segments = xml_data.policy.scope.exclusions.network_segments
		self.exclusions.ibeacons = xml_data.policy.scope.exclusions.ibeacons

	@staticmethod
	def addComputers():
		print('addcomputers', inspect.stack())




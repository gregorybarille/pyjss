from bs4 import BeautifulSoup as soup
import inspect


class Policy:

	def __init__(self, xml_data ):
		xml_data = soup(xml_data, 'xml')
		self.data = xml_data
		self.id = xml_data.policy.general.id
		self.name = xml_data.policy.general.name
		self.category = xml_data.policy.general.category
		self.scope = xml_data.policy.scope
		self.allcomputers = xml_data.policy.scope.all_computers
		self.computers = xml_data.policy.scope.computers
		self.computergroups = xml_data.policy.scope.computer_groups
		self.buildings = xml_data.policy.scope.buildings
		self.departments = xml_data.policy.scope.departments
		self.limitations = xml_data.policy.scope.limitations
		self.limitations_users = xml_data.policy.scope.limitations.users
		self.limitations_usergroups = xml_data.policy.scope.limitations.user_groups
		self.limitations.networksegments = xml_data.policy.scope.limitations.network_segments
		self.limitations.ibeacons = xml_data.policy.scope.limitations.ibeacons
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
	def addComputers(*args):
		print(args)
		for arg in args:
			print(type(arg))


	@staticmethod
	def addComputersGroups(*args):
		print('addComputersGroups')

	@staticmethod
	def addBuildings(*args):
		print('addBuildings')
	
	@staticmethod
	def addDepartments(*args):
		print('addDepartments')
	
	@staticmethod
	def excludeComputers(*args):
		print('excludeComputers')

	@staticmethod
	def excludeComputersGroups(*args):
		print('excludeComputersGroups')
	
	@staticmethod
	def excludeCBuildings(*args):
		print('excludeCBuildings')

	@staticmethod
	def excludeDepartments(*args):
		print('excludeDepartments')

	@staticmethod
	def clear_scope(policy_data):
		print('clear_scope')




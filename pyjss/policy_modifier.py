from bs4 import BeautifulSoup as soup
from pyjss.templates import default_scope_template, default_policy_template
from pyjss.objects_list import Policies


class Policy:

	def __init__(self, xml_data ):
		xml_data = soup(xml_data, 'xml')
		self.data = xml_data
		self._id = xml_data.policy.general.find('id', recursive=False).string
		self._name = xml_data.policy.general.find('name', recursive=False).string
		self._enabled = xml_data.policy.general.find('enabled', recursive=False)
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

	def __str__(self):
		return self.data.prettify()

	@property
	def name(self):
		return self._name.string

	@name.setter
	def name(self, value):
		self._name.string = value

	@property
	def id(self):
		return self._id

	@id.setter
	def id(self, value):
		self._id.string = value
	
	@property
	def enabled(self):
		return self._enabled.string

	@enabled.setter
	def enabled(self, value):
		value = value.lower()
		if value not in ['true', 'false']:
			raise ValueError
		else:
			print('setter2')
			self._enabled.string = value


	def __parse_addition(self,action_type, data_type, *args):
		if len(args) == 0:
			if action_type == 'add':
				print('No items to be added')
			elif 'remove' in action_type:
				self.data.scope.find(data_type, recursive=False).clear()
		else:
			tag_name = data_type[:(len(data_type) - 1)]
			if 'remove' in action_type:
				for arg in args:
					if 'exclude' in action_type:
						self.data.exclusions.find(data_type, recursive=False).find(tag_name, string=arg).decompose()
					else:
						#check remove one item
						self.data.scope.find(data_type, recursive=False).find(tag_name, string=arg).decompose()
			elif 'add' in action_type:
				for arg in args:
					new_tag = self.data.new_tag(tag_name)
					if type(arg) == int:
						new_sub_tag = self.data.new_tag('id')
					elif type(arg) == str:
						new_sub_tag = self.data.new_tag('name')
					else:
						raise TypeError
					new_sub_tag.string = str(arg)
					new_tag.append(new_sub_tag)
					if action_type == 'add':
						self.data.scope.find(data_type, recursive=False).append(new_tag)
					elif action_type == 'exclude':
						self.data.scope.exclusions.find(data_type, recursive=False).append(new_tag)
		return self.data

	def addComputers(self, *args):
		return self.__parse_addition('add', 'computers', *args)

	def removeComputers(self, *args):
		return self.__parse_addition('remove', 'computers', *args)

	def addComputersGroups(self, *args):
		return self.__parse_addition('add', 'computer_groups', *args)

	def removeComputersGroups(self, *args):
		return self.__parse_addition('remove', 'computer_groups', *args)

	def addBuildings(self, *args):
		return self.__parse_addition('add', 'buildings', *args)

	def removeBuildings(self, *args):
		return self.__parse_addition('remove', 'buildings', *args)

	def addDepartments(self, *args):
		return self.__parse_addition('add', 'departments', *args)

	def removeDepartments(self, *args):
		return self.__parse_addition('remove', 'departments', *args)

	def excludeComputers(self, *args):
		return self.__parse_addition('exclude', 'computers', *args)

	def removeExcludedComputers(self, *args):
		return self.__parse_addition('remove exclude', 'computers', *args)
	
	def excludeComputersGroups(self, *args):
		return self.__parse_addition('exclude', 'computer_groups', *args)

	def removeExcludedComputersGroups(self, *args):
		return self.__parse_addition('remove exclude', 'computer_groups', *args)

	def excludeBuildings(self, *args):
		return self.__parse_addition('exclude', 'buildings', *args)

	def removeExcludedBuildings(self, *args):
		return self.__parse_addition('remove exclude', 'buildings', *args)

	def excludeDepartments(self, *args):
		return self.__parse_addition('exclude', 'departments', *args)

	def removeExcludedDepartments(self, *args):
		return self.__parse_addition('remove exclude', 'departments', *args)
	
	def clear_scope(self):
		return self.data.find('scope').replace_with(soup(default_scope_template, 'xml'))

	def update(self):
		return Policies.putById(str(self.id), str(self.data))
	
	def delete(self):
		return Policies.deleteById(str(self.id))

def generatePolicy():
	return Policy(default_policy_template)

import keyring

class Credentials:

	url = ''
	username = ''
	password = ''

	def __init__(self, url, username, password):
		Credentials.url = url
		Credentials.username = username
		Credentials.password = password

	@classmethod
	def get(cls):
		return { 'url' : Credentials.url, 'username': Credentials.username, 'password': Credentials.password}

def set_credentials(url, username, password):
	try:
		keyring.set_password(url, username, password)
	except TypeError as e:
		print('The following error occured:')
		print(e)
		exit()
	else:
		return Credentials(url, username, password)

def get_credentials(url, username):
	try:
		password = keyring.get_password(url, username)
	except TypeError as e:
		print('The following error occured:')
		print(e)
		exit()
	else:
		if password != None:
			print('A password has been successully retrieved')
			return Credentials(url, username, password)
		else:
			print('There is no password stored for the url {0} and the name {1}'.format(url, password))
			exit()



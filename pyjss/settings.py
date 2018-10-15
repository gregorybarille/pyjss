import json

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
        return {'url': Credentials.url, 'username': Credentials.username, 'password': Credentials.password}


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
            print('There is no password stored for the url {0} and the name {1}'.format(
                url, password))
            exit()


def create_auth_file():
    path_file = input(
        'Provide the path of the file (including the file name): ')
    api_url = input('Provide your API url: ')
    api_username = input('Provide your API username: ')
    api_password = input('Provide your API password: ')
    data = {"api_url": api_url, "api_username": api_username,
            "api_password": api_password}
    with open(path_file, 'w+') as file:
        json.dump(data, file)


def get_auth_from_file(filename):
    try:
        with open(filename, 'r') as auth_file:
            credentials_data = json.load(auth_file)
            try:
                Credentials(credentials_data['api_url'],
                            credentials_data['api_username'], credentials_data['api_password'])
            except KeyError:
                print(
                    'The auth file should have the following format :\n{\n"url":"url_value",\n "username":"username_value",\n "password":"password_value"\n}')
                exit
            else:
                print('A password has been successully retrieved')
    except FileNotFoundError:
        choice = input(
            'The file doesn\'t exist, do you want to create it? (yes/no) ').lower()
        if choice not in ['yes', 'y']:
            exit
        else:
            create_auth_file()
    except PermissionError:
        print(
            'Youn don\'t have the permissions to read the file {0}'.format(filename))
        exit

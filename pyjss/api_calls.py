import requests
from bs4 import BeautifulSoup as soup

from pyjss.settings import Credentials


def get_call(url):
    base_url = Credentials.url
    username = Credentials.username
    password = Credentials.password
    response = requests.get(f'{base_url}JSSResource/{url}', headers={'Accept': "application/xml"}, auth=(username, password))
    if response.status_code == 200:
        return soup(response.content, 'xml')
    else:
        return response.status_code


def put_call(url, data=None):
    base_url = Credentials.url
    username = Credentials.username
    password = Credentials.password
    print(type(data))
    response = requests.put(f'{base_url}JSSResource/{url}', data, auth=(username, password))
    print(f'{base_url}JSSResource/{url}')
    if response.status_code == 201:
        print(response.content, response.status_code)
        return soup(response.content, 'xml')
    else:
        return f'Error {response.status_code}'


def post_call(url, data=None):
    base_url = Credentials.url
    username = Credentials.username
    password = Credentials.password
    response = requests.post(f'{base_url}JSSResource/{url}', data, auth=(username, password))
    if response.status_code == 201:
        return soup(response.content, 'xml')
    else:
        return f'Error {response.status_code}'


def delete_call(url, data=None):
    base_url = Credentials.url
    username = Credentials.username
    password = Credentials.password
    response = requests.delete(f'{base_url}JSSResource/{url}', auth=(username, password))
    if response.status_code == 200:
        return response.content
    else:
        return f'Error {response.status_code}'

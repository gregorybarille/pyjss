import json
import xml.etree.ElementTree as etree

import requests
from bs4 import BeautifulSoup as soup
from pyjss.settings import Credentials


def get_call(url):
    base_url = Credentials.url
    username = Credentials.username
    password = Credentials.password
    response = requests.get(
        '{0}{1}{2}'.format(base_url, 'JSSResource/', url), headers={'Accept': "application/xml"}, auth=(username, password))
    if response.status_code == 200:
        return soup(response.content, 'xml')
    else:
        return response.status_code


def put_call(url, data=None):
    base_url = Credentials.url
    username = Credentials.username
    password = Credentials.password
    print(type(data))
    response = requests.put('{0}{1}{2}'.format(
        base_url, 'JSSResource/', url), data, auth=(username, password))
    print('{0}{1}{2}'.format(base_url, 'JSSResource/', url))
    if response.status_code == 201:
        print(response.content, response.status_code)
        return soup(response.content, 'xml')
    else:
        return 'Error {0}'.format(response.status_code)


def post_call(url, data=None):
    base_url = Credentials.url
    username = Credentials.username
    password = Credentials.password
    response = requests.post('{0}{1}{2}'.format(
        base_url, 'JSSResource/', url), data, auth=(username, password))
    if response.status_code == 201:
        return soup(response.content, 'xml')
    else:
        return 'Error {0}'.format(response.status_code)


def delete_call(url, data=None):
    base_url = Credentials.url
    username = Credentials.username
    password = Credentials.password
    response = requests.delete('{0}{1}{2}'.format(
        base_url, 'JSSResource/', url), auth=(username, password))
    if response.status_code == 200:
        return response.content
    else:
        return 'Error {0}'.format(response.status_code)

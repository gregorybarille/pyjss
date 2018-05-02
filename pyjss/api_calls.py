import json
import xml.etree.ElementTree as etree

import requests

from pyjss.settings import Credentials


def get_call(url):
    base_url = Credentials.url
    username = Credentials.username
    password = Credentials.password
    response = requests.get(
        '{0}{1}'.format(base_url, url), headers={'Accept': "application/json"}, auth= ( username, password ))
    if response.status_code == 200:
        return response.json()
    else:
        return 'Error {0}'.format(response.status_code)


def put_call(url, data=None):
    base_url = Credentials.url
    username = Credentials.username
    password = Credentials.password
    response = requests.put('{0}{1}'.format(
        base_url, url), data, auth=(username, password))
    if response.status_code == 201:
        xml = etree.fromstring(response.content)
        item_id = xml.find('id').text
        print("The object has been successfully created with the following ID: {0}".format(
            item_id))
    else:
        return 'Error {0}'.format(response.status_code)

def push_call(url, data=None):
    base_url = Credentials.url
    username = Credentials.username
    password = Credentials.password
    response = requests.post('{0}{1}'.format(base_url, url), data, auth = (username, password))
    if response.status_code == 201:
        xml = etree.fromstring(response.content)
        item_id = xml.find('id').text
        print("The object has been successfully created with the following ID: {0}".format(item_id))
    else:
        return 'Error {0}'.format(response.status_code)


def delete_call(url, data=None):
    base_url = Credentials.url
    username = Credentials.username
    password = Credentials.password
    response=requests.put('{0}{1}'.format(base_url, url), data, auth = (username, password))
    if response.status_code == 200:
        return response.json()
    else:
        return 'Error {0}'.format(response.status_code)

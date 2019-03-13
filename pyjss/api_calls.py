from concurrent.futures import ThreadPoolExecutor

import requests
from bs4 import BeautifulSoup as soup

from pyjss.settings import Credentials


def fetch(call_type, args, data=None):
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(call_type, args)
        results_dict = {result[0]: result[1] for result in results}
        if len(results_dict) > 1:
            return results_dict
        else:
            return results_dict[args[0]]
        # return [result for result in results]


def get_call(arg):
    base_url = Credentials.url
    username = Credentials.username
    password = Credentials.password
    response = requests.get(f'{base_url}JSSResource/{arg}', headers={'Accept': "application/xml"}, auth=(username, password))
    if response.status_code == 200:
        return [arg, soup(response.content, 'xml')]
    else:
        return [arg, response.status_code]


def put_call(arg, data=None):
    base_url = Credentials.url
    username = Credentials.username
    password = Credentials.password
    print(type(data))
    response = requests.put(f'{base_url}JSSResource/{arg}', data, auth=(username, password))
    print(f'{base_url}JSSResource/{arg}')
    if response.status_code == 201:
        print(response.content, response.status_code)
        return [arg, soup(response.content, 'xml')]
    else:
        return [arg, response.status_code]


def post_call(arg, data=None):
    base_url = Credentials.url
    username = Credentials.username
    password = Credentials.password
    response = requests.post(f'{base_url}JSSResource/{arg}', data, auth=(username, password))
    if response.status_code == 201:
        return [arg, soup(response.content, 'xml')]
    else:
        return [arg, response.status_code]


def delete_call(arg, data=None):
    base_url = Credentials.url
    username = Credentials.username
    password = Credentials.password
    response = requests.delete(f'{base_url}JSSResource/{arg}', auth=(username, password))
    if response.status_code == 200:
        return [arg, soup(response.content, 'xml')]
    else:
        return [arg, response.status_code]

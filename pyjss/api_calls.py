from concurrent.futures import ThreadPoolExecutor

import requests
from bs4 import BeautifulSoup as soup

from pyjss.settings import Credentials


calls = {
    'get': requests.get,
    'put': requests.put,
    'post': requests.post,
    'delete': requests.delete,
}


def fetch(call_type, endpoint, args=None, data=None):
    if args:
        with ThreadPoolExecutor(max_workers=10) as executor:
            results = executor.map(make_call(call_type, endpoint), args)
            results_dict = {result[0]: result[1] for result in results}
            if len(results_dict) > 1:
                return results_dict
            else:
                return results_dict[args[0]]
    else:
        return make_call(call_type, endpoint[0])


def make_call(call_type, endpoint, arg=None, data=None):
    base_url = Credentials.url
    full_url = '/'.join(filter(None, [f'{base_url}JSSResource', endpoint, arg]))
    headers = {"Accept": "application/xml"}
    response = calls[call_type](full_url, auth=(Credentials.username, Credentials.password), headers=headers, data=data)
    if response.status_code == 200:
        if arg:
            return [arg, soup(response.content, 'xml')]
        else:
            return soup(response.content, 'xml')
    else:
        if arg:
            return [arg, response.status_code]
        else:
            return response.status_code

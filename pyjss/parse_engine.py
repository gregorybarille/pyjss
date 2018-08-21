import inspect
import sys
from pyjss.api_calls import delete_call, get_call, post_call, put_call
from pyjss.endpoints import endpoints


endpoints = {
	'id': '/id/{0}',
	'name': '/name/{0}',
	'userid': '/userid/{0}',
	'username': '/username/{0}',
	'groupid': '/groupid/{0}',
	'groupname': '/groupname/{0}',
	'siteid': '/siteid/{0}',
	'sitename': '/sitename/{0}',
	'extension':'/extension/{0}'
}
#Get function caller name :inspect.stack()[1][3]
def clean_args(args):
	print(args)
	args_list = []
	for arg in args:
		args_list.append(str(arg)) if arg != None else 'false'
	return args_list

def get_no_parameter(class_name):
	return get_call('{0}'.format(str(class_name).lower()))

def get_by_field(class_name, field, *args):
	url = str(class_name).lower() + field + args
	return get_call(url)


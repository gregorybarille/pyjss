import inspect
from pyjss.api_calls import delete_call, get_call, push_call, put_call
from pyjss.endpoints import endpoints

#Get function caller name :inspect.stack()[1][3]
def clean_args(args):
	args_list = []
	for arg in args:
		args_list.append(arg) if arg != None else 'false'
	return len(args_list),args_list

def retrieve_endpoint(args_len, args_cleaned, class_name):
	parent_function = inspect.stack()[2][3]
	if args_len == 0:
		endpoint = ''
		methods = endpoints[class_name][0]['methods']
	elif args_len == 1:
		if type(args_cleaned[0]) == int:
			endpoint = endpoints[class_name][1]['id']['endpoint']
			methods = endpoints[class_name][1]['id']['methods']
		if type(args_cleaned[0]) == str:
			endpoint = endpoints[class_name][1]['name']['endpoint']
			methods = endpoints[class_name][1]['name']['methods']
			print(endpoint, methods)
	elif args_len == 2:
		try:
			endpoint = endpoints[class_name][2][args_cleaned[1]]['endpoint']
		except KeyError:
			print('The arguments {0} is not valid'.format(args_cleaned[1]))
			return
		else:
			methods = endpoints[class_name][2][args_cleaned[1]]['methods']
	if parent_function in methods:
		return class_name.lower() + endpoint.format(*args_cleaned)
	else:
		print('The method {0} is not available for this endpoint. Use one the following {1}'.format(parent_function, methods))


def process_data(class_name, *args):
	args_len,args_cleaned = clean_args(args)
	url = retrieve_endpoint(
		args_len, args_cleaned, class_name)
	if url != None:
		print(url)
		data = get_call(url)
		print(data)


import inspect
from pyjss.api_calls import delete_call, get_call, push_call, put_call
#Get function caller name :inspect.stack()[1][3]
def clean_args(args):
	args_list = []
	for arg in args:
		args_list.append(arg) if arg != None else 'false'
	return len(args_list),args_list

def retrieve_endpoint(args_len, args_cleaned, description):
	parent_function = inspect.stack()[2][3]
	if args_len == 0:
		endpoint = description[0]['endpoint']
		methods = description[0]['methods']
	elif args_len == 1:
		if type(args_cleaned[0]) == int:
			endpoint = description[1]['id']['endpoint']
			methods = description[1]['id']['methods']
		if type(args_cleaned[0]) == str:
			endpoint = description[1]['name']['endpoint']
			methods = description[1]['name']['methods']
			print(endpoint, methods)
	elif args_len == 2:
		try:
			endpoint = description[2][args_cleaned[1]]['endpoint']
		except KeyError:
			print('The arguments {0} is not valid'.format(args_cleaned[1]))
			return
		else:
			methods = description[2][args_cleaned[1]]['methods']
	if parent_function in methods:
		return endpoint
	else:
		print('The method {0} is not available for this endpoint. Use one the following {1}'.format(parent_function, methods))


def process_data(class_details, *args):
	args_len,args_cleaned = clean_args(args)
	call_url = retrieve_endpoint(
		args_len, args_cleaned, description=class_details.description)
	if call_url != None:
		data = get_call(call_url)
		print(data)


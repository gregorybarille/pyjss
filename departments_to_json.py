import json
import time
import pyjss as p


from concurrent.futures import ThreadPoolExecutor
# p.get_credentials('https://testeduvd.jamfcloud.com/', 'gregory')
p.get_credentials('https://deploiement.edu-vd.ch/', 'gregory')


def get_departments():
    departments_list = p.Departments.get()
    print(departments_list)
    departments_list = [x.string for x in departments_list]
    return departments_list


def generate_json(departments_list):
    json_data = {'departments': departments_list}
    with open('/Users/greg/Desktop/departments.json', 'w+') as json_file:
        json.dump(json_data, json_file)


if __name__ == "__main__":
    start = time.time()
    departments_list = get_departments()
    generate_json(departments_list)
    print('It took', time.time() - start, 'seconds.')

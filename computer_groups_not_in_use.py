import csv
import time
import os
import urllib.parse
import pyjss as p
import requests
from bs4 import BeautifulSoup as soup

from concurrent.futures import ThreadPoolExecutor
# p.get_credentials('https://testeduvd.jamfcloud.com/', 'gregory')
p.get_credentials('https://deploiement.edu-vd.ch/', 'gregory')


def get_smart_groups():
    not_used = 0
    used = 0
    groups_list = p.ComputerGroups.get().find_all('computer_group')
    for group in groups_list:
        if group.is_smart.string == 'true':
            group_id = group.find('id').string
            group_name = group.find('name').string
            if 'MDM' not in group_name and 'Update' not in group_name:
                if group_id not in used_groups_dictionnary:
                    print(f'{group_name} with the id {group_id} is not used')
                    not_used += 1
                    # print(group_name + 'is not used')
                else:
                    used += 1
        else:
            pass
    print(f'Group in use {used}')
    print(f'Group not in use {not_used}')


def get_policies_groups():
    policies_list = [policy.string for policy in p.Policies.get().find_all('id')]
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(get_group_from_policies, policies_list)


def get_group_from_policies(policy_id):
    policy = p.Policies.getById(policy_id)
    policy_name = policy.name
    groups = policy.computergroups.find_all('computer_group')
    for group in groups:
        group_id = group.find('id').string
        group_name = group.find('name').string
        update_dictionnary(group_id, 'policies', policy_name)


def get_profiles_groups():
    profiles_list = [profile.string for profile in p.OsxConfigurationProfiles.get().find_all('id')]
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(get_group_from_profiles, profiles_list)


def get_group_from_profiles(profile_id):
    profile = p.OsxConfigurationProfiles.getById(profile_id)
    profile_name = profile.find('name')
    groups = profile.find('computer_groups').find_all('computer_group')
    if groups:
        for group in groups:
            group_id = group.find('id').string
            group_name = group.find('name').string
            update_dictionnary(group_id, 'profiles', profile_name)


def get_apps_groups():
    application_list = [application.string for application in p.MacApplications.get().find_all('id')]
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(get_group_from_applications, application_list)


def get_group_from_applications(application_id):
    application = p.MacApplications.getById(application_id)
    application_name = application.find('name')
    groups = application.find('computer_groups').find_all('computer_group')
    if groups:
        for group in groups:
            group_id = group.find('id').string
            group_name = group.find('name').string
            update_dictionnary(group_id, 'application', application_name)


def update_dictionnary(key, category, value):
    if key not in used_groups_dictionnary:
        used_groups_dictionnary[key] = {category: [value]}
    else:
        if category in used_groups_dictionnary[key]:
            used_groups_dictionnary[key][category].append(value)
        else:
            used_groups_dictionnary[key] = {category: [value]}


if __name__ == "__main__":
    start = time.time()
    used_groups_dictionnary = {}
    print('Checking policy')
    get_policies_groups()
    print('Checking profiles')
    get_profiles_groups()
    print('Checking application')
    get_apps_groups()
    print('Checking groups')
    get_smart_groups()
    print('It took', time.time() - start, 'seconds.')

__*PYJSS is currently in development. More details will come when the project will be more advanced.*__

More detailed info coming in the furture to the [wiki](https://github.com/sillegue/pyjss/wiki) page.

Basic usage:

**Managing credentials:**

1. Using the module [keyring](https://github.com/jaraco/keyring) to store your credentials ( Works with MacOS keychain/,Windows credential Locker, Kwallet(KDE 4/5 and others). There is one command to set the credentials and one to retrieve it:

```python
#Set credentials
pyjss.set_credentials('url', 'username', 'password')
#Retrieve credentials
pyjss.get_credentials('url', 'username', 'password)
```
2. Creating an json file locally  witht the following data
```json
{
"url":"url_value",
 "username":"username_value",
"password":"password_value"
}
```
```python
#Retrieving the credentials
pyjss.get_auth_from_file(file)
```


**Making API Calls**

The calls are based on the JAMF PRO Classic API endpoints ([Developer Portal](https://developer.jamf.com/apis/classic-api/index))
We also need to specify which kind of data to get/use (id/name/serialnumber...)

For example:

```python
pyjss.Policies.getById('PolicyTest')
```

All valid responses will be returned as a Beautiful Soup object. It's used to parse the xml.
For more information pleave refer to the [documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

**PYJSS Objects**

**Policy**

At the current stage only pyjss.Policies.getById and pyjss.Policies.getByName will create an object where you can access the following attributes:

Attributes | Value returned
------------ | -------------
id | Get the Policy ID
name | Get the Policy Name
enabled | Get the Policy status
category | Get the Policy Category
scope | Get the full Policy scope
allcomputers | Get the scope value for All Computers
computers | Get the Policy scope for computer targets
computergroups | Get the Policy scope for computergroups targets
buildings | Get the Policy scope for buildings targets
departments | Get the Policy scope for departments targets
limitations | Get limitations for the policy scope
limitations.users | Get limitations by user for policy scope
limitations.networksegments | Get limitations by networksegments for policy scope
limitations.ibeacons | Get limitations by ibeacons for policy scope
exclusions | Get exclusions from the policy scope
exclusions.computers | Get exclusions  by computers from the policy scope 
exclusions.computergroups | Get exclusions  by computergroups from the policy scope 
exclusions.buildings | Get exclusions  by buildings from the policy scope 
exclusions.departments | Get exclusions  by departments from the policy scope
exclusions.users | Get exclusions  by users from the policy scope 
exclusions.usergroups | Get exclusions  by usergroups from the policy scope
exclusions.networksegments | Get exclusions  by networksegments from the policy scope 
exclusions.ibeacons | Get exclusions  by ibeacons from the policy scope

The following functions are available on Policy objects:

:exclamation: Be carefull if you want to provide and ID it should be passed as an Integer

Function name | Action
------------ | -------------
addComputers(*args) | Add computers to scope targets
removeComputers(*args) | Remove computers from scope targets
addComputersGroups(*args) | Add computers groups to scope targets
removeComputersGroups(*args) | Remove computers groups  from scope targets
addBuildings(*args) | Add buildings to scope targets
removeBuildings(*args) | Remove buildings from scope targets
addDepartments(*args) | Add departments to scope targets
excludeComputers(*args) | Add computers to exclusions
removeExcludedComputers(*args) | Remove computers from exclusions
excludeComputersGroups(*args) | Add computer groups to exclusions
removeExcludedComputersGroups(*args) | Remove computer groups from exclusions
excludeBuildings(*args) | Add buildings to exclusions
removeExcludedBuildings(*args) | Remove buildings from exclusions
excludeDepartments(*args) | Add departments to exlusions
removeExcludedDepartments(*args) | Remove departments from exclusions
clear_scope() | Clear the entire policy scope
update() | Send the policy data to your Jamf Pro server (using PUT)
delete() | Remove the policy from your Jamf Pro server ( using DELETE )

:exclamation: When *args are expected if you call the function without passing args it will empty the specific scope section

**Additionnal informations**

The package has been tested only on python version >= 3.6 only

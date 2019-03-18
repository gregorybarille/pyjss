from pyjss.api_calls import fetch, delete_call, get_call, post_call, put_call
from pyjss.templates import default_policy_template, default_scope_template
from bs4 import BeautifulSoup as soup


class Accounts():

    @classmethod
    def get(cls):
        '''Return list of accounts'''
        return get_call(__class__.__name__.lower())

    @classmethod
    def getByUserId(cls, useriD):
        return get_call(f'{__class__.__name__.lower()}/userid/{useriD}')

    @classmethod
    def putByUserId(cls, useriD, payload):
        return put_call(f'{__class__.__name__.lower()}/userid/{useriD}', payload)

    @classmethod
    def postByUserId(cls, useriD, payload):
        return post_call(f'{__class__.__name__.lower()}/userid/{useriD}', payload)

    @classmethod
    def deleteBUserId(cls, useriD):
        return delete_call(f'{__class__.__name__.lower()}/userid/{useriD}')

    @classmethod
    def getByUserName(cls, userName):
        return get_call(f'{__class__.__name__.lower()}/username/{userName}')

    @classmethod
    def putByUserName(cls, userName, payload):
        return put_call(f'{__class__.__name__.lower()}/username/{userName}', payload)

    @classmethod
    def postByUserName(cls, userName, payload):
        return post_call(f'{__class__.__name__.lower()}/username/{userName}', payload)

    @classmethod
    def deleteByUserName(cls, userName):
        return delete_call(f'{__class__.__name__.lower()}/username/{userName}')

    @classmethod
    def getByGroupId(cls, groupID):
        return get_call(f'{__class__.__name__.lower()}/groupid/{groupID}')

    @classmethod
    def putByGroupId(cls, groupID, payload):
        return put_call(f'{__class__.__name__.lower()}/groupid/{groupID}', payload)

    @classmethod
    def postByGroupId(cls, groupID, payload):
        return post_call(f'{__class__.__name__.lower()}/groupid/{groupID}', payload)

    @classmethod
    def deleteByGroupId(cls, groupID):
        return delete_call(f'{__class__.__name__.lower()}/groupid/{groupID}')

    @classmethod
    def getByGroupName(cls, groupName):
        return get_call(f'{__class__.__name__.lower()}/groupname/{groupName}')

    @classmethod
    def putByGroupName(cls, groupName, payload):
        return put_call(f'{__class__.__name__.lower()}/groupname/{groupName}', payload)

    @classmethod
    def postByGroupName(cls, groupName, payload):
        return post_call(f'{__class__.__name__.lower()}/groupname/{groupName}', payload)

    @classmethod
    def deleteByGroupName(cls, groupName):
        return delete_call(f'{__class__.__name__.lower()}/groupname/{groupName}')


class ActivationCode():

    @classmethod
    def get(cls):
        '''Return Activation Code'''
        return get_call(__class__.__name__.lower())

    @classmethod
    def put(cls, activation_code):
        '''Return Activation Code'''
        return put_call(__class__.__name__.lower(), activation_code)


class AdvancedComputerSearches():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')


class AdvancedMobileDeviceSearches():
    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')


class AdvancedUserSearches():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')


class AllowedFileExtension():

    @classmethod
    def get(cls):
        '''Return list of accounts'''
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByExtension(cls, extension):
        return get_call(f'{__class__.__name__.lower()}/extension/{extension}')

    @classmethod
    def putByExtension(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postByExtension(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteByExtension(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')


class Buildings():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')


class ByoProfiles():
    '''verify basic object'''
    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def getBysiteId(cls, siteID):
        return get_call(f'{__class__.__name__.lower()}/siteid/{siteID}')

    @classmethod
    def putBysiteId(cls, siteID, data):
        return put_call(f'{__class__.__name__.lower()}/siteid/{siteID}', data)

    @classmethod
    def getBySiteName(cls, siteName):
        return get_call(f'{__class__.__name__.lower()}/sitename/{siteName}')

    @classmethod
    def putBySiteName(cls, siteName, data):
        return put_call(f'{__class__.__name__.lower()}/sitename/{siteName}', data)


class Categories():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')


class Classes():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')


class CommandFlush():

    @classmethod
    def deleteById(cls, group_type, id_items, status):
        '''group_type could be one of the following: computers, computergroups, mobiledevices, mobiledevicegroups
        id_items could a single or multiple value ( separated by comma )
        status could be one of the following: Pending, Failed or Pending+Failed
        '''
        return delete_call(f'{__class__.__name__.lower()}/{group_type}/id/{id_items}/status/{status}')


class ComputerApplications():

    @classmethod
    def getApp(cls, application):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/application/{application}')

    @classmethod
    def getAppInfo(cls, application, inventory_items):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/application/{application}/inventory/{inventory_items}')

    @classmethod
    def getAppVersion(cls, application, version):
        return get_call(f'{__class__.__name__.lower()}/application/{application}/version/{version}')

    @classmethod
    def getAppVersionInfo(cls, application, version, info_items):
        return get_call(f'{__class__.__name__.lower()}/application/{application}/version/{version}/inventory/{info_items}')


class ComputerApplicationUsage():

    @classmethod
    def getById(cls, id_item, start_date, en_date):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}/{start_date}_{en_date}')

    @classmethod
    def getByName(cls, name_item, start_date, en_date):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}/{start_date}_{en_date}')

    @classmethod
    def getByUdid(cls, udid_item, start_date, en_date):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/udid/{udid_item}/{start_date}_{en_date}')

    @classmethod
    def getBySerial(cls, serial_item, start_date, en_date):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/serialnumber/{serial_item}/{start_date}_{en_date}')

    @classmethod
    def getByMac(cls, mac_item, start_date, en_date):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/macaddress/{mac_item}/{start_date}_{en_date}')


class ComputerCheckin():

    @classmethod
    def get(cls):
        ''''''
        return get_call(__class__.__name__.lower())

    @classmethod
    def put(cls, checkin):
        ''''''
        return put_call(__class__.__name__.lower(), checkin)


class ComputerCommands():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)


class ComputerConfigurations():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')


class ComputerExtensionAttributes():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')


class ComputerGroups():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')


class ComputerHardwareSoftwareReports():

    @classmethod
    def getById(cls, id_item, start_date, en_date):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}/{start_date}_{en_date}')

    @classmethod
    def getByIdSubset(cls, id_item, start_date, en_date, subset_items):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}/{start_date}_{en_date}/subset/{subset_items}')

    @classmethod
    def getByName(cls, name_item, start_date, en_date):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}/{start_date}_{en_date}')

    @classmethod
    def getByUdid(cls, udid_item, start_date, en_date):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/udid/{udid_item}/{start_date}_{en_date}')

    @classmethod
    def getBySerial(cls, serial_item, start_date, en_date):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/serialnumber/{serial_item}/{start_date}_{en_date}')

    @classmethod
    def getByMac(cls, mac_item, start_date, en_date):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/macaddress/{mac_item}/{start_date}_{en_date}')


class ComputerHistory():

    @classmethod
    def getById(cls, id_item):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getSubset(cls, item_type, item, subset_items):
        '''Item_type could be id/name/udid/serialnumber or macaddress'''
        return get_call(f'{__class__.__name__.lower()}/{item_type}/{item}/subset/{subset_items}')

    @classmethod
    def getByName(cls, name_item):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def getByUdid(cls, udid_item):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/udid/{udid_item}'.format(__class__.__name__.lower(), udid_item))

    @classmethod
    def getBySerial(cls, serial_item):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/serialnumber/{serial_item}')

    @classmethod
    def getByMac(cls, mac_item):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/macaddress/{mac_item}')


class ComputerInventoryCollection():

    @classmethod
    def get(cls):
        '''Return Activation Code'''
        return get_call(__class__.__name__.lower())

    @classmethod
    def put(cls, settings):
        '''Return Activation Code'''
        return put_call(__class__.__name__.lower(), settings)


class ComputerInvitations():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def getByInvitation(cls, invitation_item):
        return get_call(f'{__class__.__name__.lower()}/invitation/{invitation_item}')

    @classmethod
    def postByInvitation(cls, invitation_item, data):
        return post_call(f'{__class__.__name__.lower()}/invitation/{invitation_item}', data)

    @classmethod
    def deleteInvitation(cls, invitation_item):
        return delete_call(f'{__class__.__name__.lower()}/invitation/{invitation_item}')


class ComputerManagement():

    @classmethod
    def getById(cls, id_item):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getSubset(cls, item_type, item, subset_items):
        '''Item_type could be id/name/udid/serialnumber or macaddress'''
        return get_call(f'{__class__.__name__.lower()}/{item_type}/{item}/subset/{subset_items}')

    @classmethod
    def getByIdUsername(cls, id_item, username):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}/username/{username}')

    @classmethod
    def getByIdPatchFilter(cls, id_item, filter_item):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}/patchfilter/{filter_item}/')

    @classmethod
    def getSubsetByUsername(cls, username, item_types, item, subset_items):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/{item_types}/{item}/username/{username}/subset/{subset_items}')

    @classmethod
    def getByName(cls, name_item):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def getByUdid(cls, udid_item):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/udid/{udid_item}')

    @classmethod
    def getBySerial(cls, serial):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/serialnumber/{serial}')

    @classmethod
    def getByMac(cls, mac_address):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/macaddress/{mac_address}')


class ComputerReports():
    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')


class Computers():

    @classmethod
    def getListID(cls):
        '''Return list of accounts'''
        data = get_call(__class__.__name__.lower())
        computer_list = []
        for computer in data['computers']:
            computer_list.append(computer['id'])
        return computer_list

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def getMoreInfo(cls):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/subset/basic')

    @classmethod
    def getByMatch(cls, match_item):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/match/{match_item}')

    @classmethod
    def getByMatchName(cls, match_name):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/match/name/{match_name}')

    @classmethod
    def getSubset(cls, item_type, item, subset_items):
        '''Item_type could be id/name/udid/serialnumber or macaddress'''
        return get_call(f'{__class__.__name__.lower()}/{item_type}/{item}/subset/{subset_items}')

    @classmethod
    def getByUdid(cls, udid_item):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/udid/{udid_item}')

    @classmethod
    def putByUdid(cls, udid_item, data):
        '''Return Advanced searches'''
        return put_call(f'{__class__.__name__.lower()}/udid/{udid_item}', data)

    @classmethod
    def postByUdid(cls, udid_item, data):
        '''Return Advanced searches'''
        return post_call(f'{__class__.__name__.lower()}/udid/{udid_item}', data)

    @classmethod
    def deleteByUdid(cls, udid_item):
        '''Return Advanced searches'''
        return delete_call(f'{__class__.__name__.lower()}/udid/{udid_item}')

    @classmethod
    def getBySerial(cls, serial_item):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/serialnumber/{serial_item}')

    @classmethod
    def putBySerial(cls, serial_item, data):
        '''Return Advanced searches'''
        return put_call(f'{__class__.__name__.lower()}/serialnumber/{serial_item}', data)

    @classmethod
    def postBySerial(cls, serial_item, data):
        '''Return Advanced searches'''
        return post_call(f'{__class__.__name__.lower()}/serialnumber/{serial_item}', data)

    @classmethod
    def deleteBySerial(cls, serial_item):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/serialnumber/{serial_item}')

    @classmethod
    def getByMac(cls, mac_item):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/macaddress/{mac_item}')

    @classmethod
    def putByMac(cls, mac_item, data):
        '''Return Advanced searches'''
        return put_call(f'{__class__.__name__.lower()}/macaddress/{mac_item}', data)

    @classmethod
    def postByMac(cls, mac_item, data):
        '''Return Advanced searches'''
        return post_call(f'{__class__.__name__.lower()}/macaddress/{mac_item}', data)

    @classmethod
    def deleteByMac(cls, mac_item):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/macaddress/{mac_item}')


class Departments():
    """Test"""
    @classmethod
    def get(cls):
        return fetch('get', [__class__.__name__.lower()])

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')


class DirectoryBindings():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')


class DiskEncryptionConfigurations():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')


class DistributionPoints():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')


class DockItems():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')


class Ebooks():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def getSubset(cls, item_type, item, subset_items):
        '''Item_type could be id/name/udid/serialnumber or macaddress'''
        return get_call(f'{__class__.__name__.lower()}/{item_type}/{item}/subset/{subset_items}')


class FileUploads():
    ''' Only post method '''
    pass


class GsxConnexion():

    @classmethod
    def get(cls):
        ''''''
        return get_call(__class__.__name__.lower())

    @classmethod
    def put(cls, settings):
        ''''''
        return put_call(__class__.__name__.lower(), settings)


class HealthCareListener():
    """ to do """
    @classmethod
    def get(cls):
        '''Return Advanced searches'''
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)


class HealthCareListenerRule():

    @classmethod
    def get(cls):
        '''Return Advanced searches'''
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')


class Ibeacons():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')


class InfrastructureManager():

    @classmethod
    def get(cls):
        '''Return Advanced searches'''
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)


class JsonWebTokenConfigurations():

    @classmethod
    def get(cls):
        '''Return Advanced searches'''
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')


class LdapServers():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def getUser(cls, server_item, user_name):
        '''Return Advanced searches'''
        if type(server_item) == int:
            return get_call(f'{__class__.__name__.lower()}/id/{1}/user/{2}'.format(__class__.__name__.lower(), server_item, user_name))
        else:
            return get_call(f'{__class__.__name__.lower()}/name/{1}/user/{2}'.format(__class__.__name__.lower(), server_item, user_name))

    @classmethod
    def getByGroup(cls, server_item, group_name):
        '''Return Advanced searches'''
        if type(server_item) == int:
            return get_call(f'{__class__.__name__.lower()}/id/{server_item}/group/{group_name}')
        else:
            return get_call(f'{__class__.__name__.lower()}/name/{server_item}/group/{group_name}')

    @classmethod
    def getUserByGroup(cls, server_item, group_name, user_name):
        '''Return Advanced searches'''
        if type(server_item) == int:
            return get_call(f'{__class__.__name__.lower()}/id/{server_item}/group/{group_name}/user/{user_name}')
        else:
            return get_call(f'{__class__.__name__.lower()}/name/{server_item}/group/{group_name}/user/{user_name}')


class LicencedSoftware():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')


class LogFlush():
    ''' to be done'''
    @classmethod
    def deleteAllPolicies(cls, interval):
        '''For interval the supported values are a combination of [Zero, One, Two, Three, Six] and [Days, Weeks, Months, Years].'''
        return delete_call(f'{__class__.__name__.lower()}/policy/interval/{interval}')

    @classmethod
    def deletePolicy(cls, id_item, interval):
        '''For interval the supported values are a combination of [Zero, One, Two, Three, Six] and [Days, Weeks, Months, Years].'''
        return delete_call(f'{__class__.__name__.lower()}/policy/id/{id_item}/interval/{interval}')


class MacApplications():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def getSubset(cls, item_type, item, subset_items):
        '''Item_type could be id/name/udid/serialnumber or macaddress'''
        return get_call(f'{__class__.__name__.lower()}/{item_type}/{item}/subset/{subset_items}')


class ManagedPreferenceProfiles():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def getSubset(cls, item_type, item, subset_items):
        '''Item_type could be id/name'''
        return get_call(f'{__class__.__name__.lower()}/{item_type}/{item}/subset/{subset_items}')


class MobileDeviceApplications():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        response = get_call(f'{__class__.__name__.lower()}/id/{id_item}')
        if type(response) == int:
            return response
        else:
            return MobileApplication(response)

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        response = get_call(f'{__class__.__name__.lower()}/name/{name_item}')
        if type(response) == int:
            return response
        else:
            print(type(response))
            return MobileApplication(response)

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def getSubset(cls, item_type, item, subset_items):
        '''Item_type could be id/name or bundleid'''
        return get_call(f'{__class__.__name__.lower()}/{item_type}/{item}/subset/{subset_items}')

    @classmethod
    def getByBundleid(cls, id_item):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/bundleid/{id_item}')

    @classmethod
    def putByBundleid(cls, id_item, data):
        '''Return Advanced searches'''
        return put_call(f'{__class__.__name__.lower()}/bundleid/{id_item}', data)

    @classmethod
    def deleteByBundleid(cls, id_item):
        '''Return Advanced searches'''
        return delete_call(f'{__class__.__name__.lower()}/bundleid/{id_item}')

    @classmethod
    def getByBundleid_version(cls, id_item, version_item):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/bundleid/{id_item}/version/{version_item}')

    @classmethod
    def putByBundleid_version(cls, id_item, version_item, data):
        '''Return Advanced searches'''
        return put_call(f'{__class__.__name__.lower()}/bundleid/{id_item}/version/{version_item}', data)

    @classmethod
    def deleteByBundleid_version(cls, id_item, version_item):
        '''Return Advanced searches'''
        return delete_call(f'{__class__.__name__.lower()}/bundleid/{id_item}/version/{version_item}')


class MobileApplication:

    def __init__(self, xml_data):
        self.data = xml_data
        self._id = xml_data.mobile_device_application.general.find('id', recursive=False)
        self._name = xml_data.mobile_device_application.general.find('name', recursive=False)
        self._site = xml_data.mobile_device_application.general.find('site', recursive=False)
        self._enabled = xml_data.mobile_device_application.general.find('enabled', recursive=False)
        self._version = xml_data.mobile_device_application.general.version
        self._free = xml_data.mobile_device_application.general.free
        self._bundle_id = xml_data.mobile_device_application.general.bundle_id
        self._itunes_store_url = xml_data.mobile_device_application.general.itunes_store_url
        self._category = xml_data.mobile_device_application.general.category
        self._make_available_after_install = xml_data.mobile_device_application.general.make_available_after_install
        self._itunes_country_region = xml_data.mobile_device_application.general.itunes_country_region
        self._itunes_sync_time = xml_data.mobile_device_application.general.itunes_sync_time
        self._deployment_type = xml_data.mobile_device_application.general.deployment_type
        self._deploy_automatically = xml_data.mobile_device_application.general.deploy_automatically
        self._deploy_as_managed_app = xml_data.mobile_device_application.general.deploy_as_managed_app
        self._remove_app_when_mdm_profile_is_removed = xml_data.mobile_device_application.general.remove_app_when_mdm_profile_is_removed
        self._prevent_backup_of_app_data = xml_data.mobile_device_application.general.prevent_backup_of_app_data
        self._keep_description_and_icon_up_to_date = xml_data.mobile_device_application.general.keep_description_and_icon_up_to_date
        self._keep_app_updated_on_devices = xml_data.mobile_device_application.general.keep_app_updated_on_devices
        self._take_over_management = xml_data.mobile_device_application.general.take_over_management
        self._host_externally = xml_data.mobile_device_application.general.host_externally
        self._external_url = xml_data.mobile_device_application.general.external_url
        self._self_service = xml_data.mobile_device_application.self_service
        self._self_service_description = xml_data.mobile_device_application.self_service.self_service_description
        self._feature_on_main_page = xml_data.mobile_device_application.self_service.feature_on_main_page
        self._self_service_categories = xml_data.mobile_device_application.self_service.self_service_categories
        self._notification = xml_data.mobile_device_application.self_service.notification
        self._notification_subject = xml_data.mobile_device_application.self_service.notification_subject
        self._notification_message = xml_data.mobile_device_application.self_service.notification_message
        self._vpp = xml_data.mobile_device_application.vpp
        self._assign_vpp_device_based_licenses = xml_data.mobile_device_application.vpp.assign_vpp_device_based_licenses
        self._vpp_admin_account_id = xml_data.mobile_device_application.vpp.vpp_admin_account_id
        self.scope = xml_data.policy.scope
        self.allcomputers = xml_data.policy.scope.all_computers
        self.computers = xml_data.policy.scope.computers
        self.computergroups = xml_data.policy.scope.computer_groups
        self.buildings = xml_data.policy.scope.buildings
        self.departments = xml_data.policy.scope.departments
        self.limitations = xml_data.policy.scope.limitations
        self.limitations_users = xml_data.policy.scope.limitations.users
        self.limitations_usergroups = xml_data.policy.scope.limitations.user_groups
        self.limitations.networksegments = xml_data.policy.scope.limitations.network_segments
        self.limitations.ibeacons = xml_data.policy.scope.limitations.ibeacons
        self.exclusions = xml_data.policy.scope.exclusions
        self.exclusions.computers = xml_data.policy.scope.exclusions.computers
        self.exclusions.computergroups = xml_data.policy.scope.exclusions.computer_groups
        self.exclusions.buildings = xml_data.policy.scope.exclusions.buildings
        self.exclusions.departments = xml_data.policy.scope.exclusions.departments
        self.exclusions.users = xml_data.policy.scope.exclusions.users
        self.exclusions.user_groups = xml_data.policy.scope.exclusions.user_groups
        self.exclusions.network_segments = xml_data.policy.scope.exclusions.network_segments
        self.exclusions.ibeacons = xml_data.policy.scope.exclusions.ibeacons

    def __repr__(self):
        return str(self.data.prettify())

    @property
    def name(self):
        return self._name.string

    @name.setter
    def name(self, value):
        self._name.string = value

    @property
    def id(self):
        return self._id.string

    @id.setter
    def id(self, value):
        self._id.string = str(value)

    @property
    def enabled(self):
        return self._enabled.string

    @enabled.setter
    def enabled(self, value):
        value = value.lower()
        if value not in ['true', 'false']:
            raise ValueError
        else:
            self._enabled.string = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if type(value) == int:
            self._category.find('id').string = str(value)
            self._category.find('name').decompose()
        elif type(value) == str:
            try:
                self._category.find('name').string = value
            except AttributeError:
                new_tag = self.data.new_tag('name')
                new_tag.string = value
                self._category.append(new_tag)

    @category.deleter
    def category(self):
        self._category.find('id').string = '-1'
        self._category.find('name').string = 'None'

    @property
    def site(self):
        return self._site

    @site.setter
    def site(self, value):
        if type(value) == int:
            print('test')
            self._site.find('id').string = str(value)
            self._site.find('name').decompose()
        elif type(value) == str:
            try:
                self._site.find('name').string = value
            except AttributeError:
                new_tag = self.data.new_tag('name')
                new_tag.string = value
                self._site.append(new_tag)

    @site.deleter
    def site(self):
        self._site.find('id').string = '-1'
        self._site.find('name').string = 'None'

    @property
    def free(self):
        return self._free.string

    @free.setter
    def free(self, value):
        value = value.lower()
        if value not in ['true', 'false']:
            raise ValueError
        else:
            self._free.string = value

    @property
    def version(self):
        return self._version.string

    @version.setter
    def version(self, value):
        self._version.string = str(value)

    @property
    def bundle_id(self):
        return self._bundle_id.string

    @bundle_id.setter
    def bundle_id(self, value):
        self._bundle_id.string = str(value)

    @property
    def itunes_store_url(self):
        return self._itunes_store_url.string

    @itunes_store_url.setter
    def itunes_store_url(self, value):
        self._itunes_store_url.string = str(value)

    def _create_tag(self, tag_name, arg):
        new_data_type = self.data.new_tag(tag_name)
        if type(arg) == int:
            new_sub_tag = self.data.new_tag('id')
        elif type(arg) == str:
            new_sub_tag = self.data.new_tag('name')
        new_sub_tag.string = str(arg)
        new_data_type.append(new_sub_tag)
        return new_data_type

    def _create_secondary_tag(self, tag_name, secondary_tag, secondary_arg, item):
        new_data_type = self.data.new_tag(tag_name)
        new_secondary_tag = self.data.new_tag(secondary_tag)
        if type(item) == int:
            new_sub_tag = self.data.new_tag('id')
        elif type(item) == str:
            new_sub_tag = self.data.new_tag('name')
        new_sub_tag.string = str(item)
        new_secondary_tag.string = str(secondary_arg)
        new_data_type.append(new_sub_tag)
        new_data_type.append(new_secondary_tag)
        return new_data_type

    def addComputers(self, *computers):
        arg_tuple = tuple(filter(lambda x: not self.computers.find(string=x), computers))
        tuple(map(lambda x: self.computers.append(self._create_tag('computer', x)), arg_tuple))

    def removeComputers(self, *computers):
        tuple(map(lambda x: self.computers.find(string=x).find_parent('computer').decompose(), computers))

    def addComputersGroups(self, *computersgroups):
        arg_tuple = tuple(filter(lambda x: not self.computergroups.find(string=x), computersgroups))
        tuple(map(lambda x: self.computergroups.append(self._create_tag('computer_group', x)), arg_tuple))

    def removeComputersGroups(self, *computersgroups):
        tuple(map(lambda x: self.computergroups.find(string=x).find_parent('computer_group').decompose(), computersgroups))

    def addBuildings(self, *buildings):
        arg_tuple = tuple(filter(lambda x: not self.buildings.find(string=x), buildings))
        tuple(map(lambda x: self.buildings.append(self._create_tag('building', x)), arg_tuple))

    def removeBuildings(self, *buildings):
        tuple(map(lambda x: self.buildings.find(string=x).find_parent('building').decompose(), buildings))

    def addDepartments(self, *departments):
        arg_tuple = tuple(filter(lambda x: not self.departments.find(string=x), departments))
        tuple(map(lambda x: self.departments.append(self._create_tag('department', x)), arg_tuple))

    def removeDepartments(self, *departments):
        tuple(map(lambda x: self.buildings.find(string=x).find_parent('department').decompose(), departments))

    def excludeComputers(self, *computers):
        arg_tuple = tuple(filter(lambda x: not self.exclusions.computers.find(string=x), computers))
        tuple(map(lambda x: self.exclusions.computers.append(self._create_tag('computer', x)), arg_tuple))

    def removeExcludedComputers(self, *computers):
        tuple(map(lambda x: self.exclusions.computers.find(string=x).find_parent('computer').decompose(), computers))

    def excludeComputersGroups(self, *computersgroups):
        arg_tuple = tuple(filter(lambda x: not self.exclusions.computergroups.find(string=x), computersgroups))
        tuple(map(lambda x: self.exclusions.computergroups.append(self._create_tag('computer_group', x)), arg_tuple))

    def removeExcludedComputersGroups(self, *computersgroups):
        tuple(map(lambda x: self.exclusions.computergroups.find(string=x).find_parent('computer_group').decompose(), computersgroups))

    def excludeBuildings(self, *buildings):
        arg_tuple = tuple(filter(lambda x: not self.exclusions.buildings.find(string=x), buildings))
        tuple(map(lambda x: self.exclusions.buildings.append(self._create_tag('building', x)), arg_tuple))

    def removeExcludedBuildings(self, *buildings):
        tuple(map(lambda x: self.exclusions.buildings.find(string=x).find_parent('building').decompose(), buildings))

    def excludeDepartments(self, *departments):
        arg_tuple = tuple(filter(lambda x: not self.exclusions.departments.find(string=x), departments))
        tuple(map(lambda x: self.exclusions.departments.append(self._create_tag('department', x)), arg_tuple))

    def removeExcludedDepartments(self, *args):
        tuple(map(lambda x: self.exclusions.departments.find(string=x).find_parent('department').decompose(), args))

    def update(self):
        return MobileDeviceApplications.putById(str(self.id), str(self.data))

    def delete(self):
        return MobileDeviceApplications.deleteById(str(self.id))


class MobileDeviceCommands():
    ''' post to be done '''
    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def getByUdid(cls, udid):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/udid/{udid}')

    @classmethod
    def getByCommand(cls, command):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/command/{command}')


class MobileDeviceConfigurationProfiles():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def getSubset(cls, item_type, item, subset_items):
        '''Item_type could be id/name'''
        return get_call(f'{__class__.__name__.lower()}/{item_type}/{item}/subset/{subset_items}')


class MobileDeviceEnrollementProfiles():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def getSubset(cls, item_type, item, subset_items):
        '''Item_type could be id/name or invitation'''
        return get_call(f'{__class__.__name__.lower()}/{item_type}/{item}/subset/{subset_items}')

    @classmethod
    def getByInvitation(cls, invitation):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/invitation/{invitation}')

    @classmethod
    def putByInvitation(cls, invitation, data):
        '''Return Advanced searches'''
        return put_call(f'{__class__.__name__.lower()}/invitation/{invitation}', data)

    @classmethod
    def postByInvitation(cls, invitation, data):
        '''Return Advanced searches'''
        return post_call(f'{__class__.__name__.lower()}/invitation/{invitation}', data)

    @classmethod
    def deleteInvitation(cls, invitation):
        return delete_call(f'{__class__.__name__.lower()}/invitation/{invitation}')


class MobileDeviceExtensionAttributes():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')


class MobileDeviceGroups():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')


class MobileDeviceHistory():

    @classmethod
    def getById(cls, id_item):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def getByUdid(cls, udid_item):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/udid/{udid_item}')

    @classmethod
    def getBySerial(cls, serial_item):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/serialnumber/{serial_item}')

    @classmethod
    def getByMac(cls, mac_item):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/macaddress/{mac_item}')

    @classmethod
    def getSubset(cls, item_type, item, subset_items):
        '''Item_type could be id/name/udid/serialnumber/macaddress'''
        return get_call(f'{__class__.__name__.lower()}/{item_type}/{item}/subset/{subset_items}')


class MobileDeviceInvitations():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByInvitation(cls, invitation_item):
        return get_call(f'{__class__.__name__.lower()}/invitation/{invitation_item}')

    @classmethod
    def putByInvitation(cls, invitation_item, data):
        return put_call(f'{__class__.__name__.lower()}/invitation/{invitation_item}', data)

    @classmethod
    def postByInvitation(cls, invitation_item, data):
        return post_call(f'{__class__.__name__.lower()}/invitation/{invitation_item}', data)

    @classmethod
    def deleteByInvitation(cls, invitation_item):
        return delete_call(f'{__class__.__name__.lower()}/invitation/{invitation_item}')


class MobileDeviceProvisionningProfiles():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def getByUdid(cls, udid_item):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/udid/{udid_item}')

    @classmethod
    def putByUdid(cls, udid_item, data):
        '''Return Advanced searches'''
        return put_call(f'{__class__.__name__.lower()}/udid/{udid_item}', data)

    @classmethod
    def postByUdid(cls, udid_item, data):
        '''Return Advanced searches'''
        return post_call(f'{__class__.__name__.lower()}/udid/{udid_item}', data)

    @classmethod
    def deleteByUdid(cls, udid_item):
        '''Return Advanced searches'''
        return delete_call(f'{__class__.__name__.lower()}/udid/{udid_item}')

    @classmethod
    def getSubset(cls, item_type, item, subset_items):
        '''Item_type could be id/name/udid'''
        return get_call(f'{__class__.__name__.lower()}/{item_type}/{item}/subset/{subset_items}')


class MobileDevices():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def getSubset(cls, item_type, item, subset_items):
        '''Item_type could be id/name/udid/serialnumber or macaddress'''
        return get_call(f'{__class__.__name__.lower()}/{item_type}/{item}/subset/{subset_items}')

    @classmethod
    def getByUdid(cls, udid_item):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/udid/{udid_item}')

    @classmethod
    def putByUdid(cls, udid_item, data):
        '''Return Advanced searches'''
        return put_call(f'{__class__.__name__.lower()}/udid/{udid_item}', data)

    @classmethod
    def postByUdid(cls, udid_item, data):
        '''Return Advanced searches'''
        return post_call(f'{__class__.__name__.lower()}/udid/{udid_item}', data)

    @classmethod
    def deleteByUdid(cls, udid_item):
        '''Return Advanced searches'''
        return delete_call(f'{__class__.__name__.lower()}/udid/{udid_item}')

    @classmethod
    def getBySerial(cls, serial_item):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/serialnumber/{serial_item}')

    @classmethod
    def putBySerial(cls, serial_item, data):
        '''Return Advanced searches'''
        return put_call(f'{__class__.__name__.lower()}/serialnumber/{serial_item}', data)

    @classmethod
    def postBySerial(cls, serial_item, data):
        '''Return Advanced searches'''
        return post_call(f'{__class__.__name__.lower()}/serialnumber/{serial_item}', data)

    @classmethod
    def deleteBySerial(cls, serial_item):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/serialnumber/{serial_item}')

    @classmethod
    def getByMac(cls, mac_item):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/macaddress/{mac_item}')

    @classmethod
    def putByMac(cls, mac_item, data):
        '''Return Advanced searches'''
        return put_call(f'{__class__.__name__.lower()}/macaddress/{mac_item}', data)

    @classmethod
    def postByMac(cls, mac_item, data):
        '''Return Advanced searches'''
        return post_call(f'{__class__.__name__.lower()}/macaddress/{mac_item}', data)

    @classmethod
    def deleteByMac(cls, mac_item):
        '''Return Advanced searches'''
        return get_call(f'{__class__.__name__.lower()}/macaddress/{mac_item}')


class NetbootServers():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')


class NetworkSegments():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')


class OsxConfigurationProfiles():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def getSubset(cls, item_type, item, subset_items):
        '''Item_type could be id/name'''
        return get_call(f'{__class__.__name__.lower()}/{item_type}/{item}/subset/{subset_items}')


class Packages():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')


class PatchAvailableTitles():

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/sourceid/{id_item}')


class PatchExternalSources():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')


class PatchInternalSources():
    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')


class PatchReports():

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def getByVersion(cls, item_type, item, version):
        '''Item_type could be id/name'''
        return get_call(f'{__class__.__name__.lower()}/{item_type}/{item}/version/{version}')


class PatchSoftwareTitles():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')


class PatchPolicies():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def getSubset(cls, id_item, subset_items):
        '''Item_type could be id/name/'''
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}/subset/{subset_items}')

    @classmethod
    def getBySoftwareConfigId(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/softwaretitleconfigid/id/{id_item}')

    @classmethod
    # ToCorrect. Needs Data Verify API
    def postBySoftwareConfigId(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/softwaretitleconfigid/id/{id_item}')


class Peripherals():

    @classmethod
    def get(cls):
        '''Return list of accounts'''
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getSubset(cls, id_item, subset_items):
        '''Item_type could be id/name/udid/serialnumber or macaddress'''
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}/subset/{subset_items}')

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')


class PeripheralsTypes():

    @classmethod
    def get(cls):
        '''Return list of accounts'''
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')


class Policies():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        response = get_call(f'{__class__.__name__.lower()}/id/{id_item}')
        if type(response) == int:
            return response
        else:
            return Policy(response)

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        response = get_call(f'{__class__.__name__.lower()}/name/{name_item}')
        if type(response) == int:
            return response
        else:
            return Policy(response)

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def getSubset(cls, item_type, item, subset_items):
        '''Item_type could be id/name'''
        return get_call(f'{__class__.__name__.lower()}/{item_type}/{item}/subset/{subset_items}')

    @classmethod
    def getByCategory(cls, category):
        return get_call(f'{__class__.__name__.lower()}/category/{category}')

    @classmethod
    def getByCreator(cls, creator_name):
        return get_call(f'{__class__.__name__.lower()}/createdBy/{creator_name}')


class Policy:

    def __init__(self, xml_data):
        self.data = xml_data
        self._id = xml_data.policy.general.find('id', recursive=False)
        self._name = xml_data.policy.general.find('name', recursive=False)
        self._enabled = xml_data.policy.general.find('enabled', recursive=False)
        self._site = xml_data.policy.general.find('site', recursive=False)
        self._category = xml_data.policy.general.category
        self._trigger_checkin = xml_data.policy.general.find('trigger_checkin', recursive=False)
        self._trigger_enrollment_complete = xml_data.policy.general.find('trigger_enrollment_complete', recursive=False)
        self._trigger_login = xml_data.policy.general.find('trigger_login', recursive=False)
        self._trigger_logout = xml_data.policy.general.find('trigger_logout', recursive=False)
        self._trigger_network_state_changed = xml_data.policy.general.find('trigger_network_state_changed', recursive=False)
        self._trigger_startup = xml_data.policy.general.find('trigger_startup', recursive=False)
        self._trigger_other = xml_data.policy.general.find('trigger_other', recursive=False)
        self._offline = xml_data.policy.general.find('offline', recursive=False)
        self._frequency = xml_data.policy.general.find('frequency', recursive=False)
        self._target_drive = xml_data.policy.general.find('target_drive', recursive=False)
        self.packages = xml_data.policy.find('packages')
        self.scripts = xml_data.policy.find('scripts')
        self.printers = xml_data.policy.find('printers', recursive=False)
        self.bindings = xml_data.policy.find('directory_bindings')
        self.maintenance = xml_data.policy.find('maintenance')
        self._update_inventory = xml_data.policy.find('maintenance').find('recon')
        self._reset_computer_name = xml_data.policy.find('maintenance').find('reset_name')
        self._install_cached_packages = xml_data.policy.find('maintenance').find('install_all_cached_packages')
        self._fix_permissions = xml_data.policy.find('maintenance').find('permissions')
        self._fix_by_host = xml_data.policy.find('maintenance').find('byhost')
        self._fix_system_caches = xml_data.policy.find('maintenance').find('system_cache')
        self._fix_user_caches = xml_data.policy.find('maintenance').find('user_cache')
        self._verify_disk = xml_data.policy.find('maintenance').find('verify')
        self.files_processes = xml_data.policy.find('files_processes')
        self._search_by_path = xml_data.policy.find('files_processes').find('search_by_path')
        self._delete_file = xml_data.policy.find('files_processes').find('delete_file')
        self._search_by_filename = xml_data.policy.find('files_processes').find('locate_file')
        self._update_locate_database = xml_data.policy.find('files_processes').find('update_locate_database')
        self._search_spotlight = xml_data.policy.find('files_processes').find('spotlight_search')
        self._search_process = xml_data.policy.find('files_processes').find('search_for_process')
        self._kill_process = xml_data.policy.find('files_processes').find('kill_process')
        self._run_command = xml_data.policy.find('files_processes').find('run_command')
        self.scope = xml_data.policy.scope
        self.allcomputers = xml_data.policy.scope.all_computers
        self.computers = xml_data.policy.scope.computers
        self.computergroups = xml_data.policy.scope.computer_groups
        self.buildings = xml_data.policy.scope.buildings
        self.departments = xml_data.policy.scope.departments
        self.limitations = xml_data.policy.scope.limitations
        self.limitations_users = xml_data.policy.scope.limitations.users
        self.limitations_usergroups = xml_data.policy.scope.limitations.user_groups
        self.limitations.networksegments = xml_data.policy.scope.limitations.network_segments
        self.limitations.ibeacons = xml_data.policy.scope.limitations.ibeacons
        self.exclusions = xml_data.policy.scope.exclusions
        self.exclusions.computers = xml_data.policy.scope.exclusions.computers
        self.exclusions.computergroups = xml_data.policy.scope.exclusions.computer_groups
        self.exclusions.buildings = xml_data.policy.scope.exclusions.buildings
        self.exclusions.departments = xml_data.policy.scope.exclusions.departments
        self.exclusions.users = xml_data.policy.scope.exclusions.users
        self.exclusions.user_groups = xml_data.policy.scope.exclusions.user_groups
        self.exclusions.network_segments = xml_data.policy.scope.exclusions.network_segments
        self.exclusions.ibeacons = xml_data.policy.scope.exclusions.ibeacons

    def __repr__(self):
        return str(self.data.prettify())

    @property
    def name(self):
        return self._name.string

    @name.setter
    def name(self, value):
        self._name.string = value

    @property
    def id(self):
        return self._id.string

    @id.setter
    def id(self, value):
        self._id.string = str(value)

    @property
    def enabled(self):
        return self._enabled.string

    @enabled.setter
    def enabled(self, value):
        value = value.lower()
        if value not in ['true', 'false']:
            raise ValueError
        else:
            self._enabled.string = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if type(value) == int:
            self._category.find('id').string = str(value)
            self._category.find('name').decompose()
        elif type(value) == str:
            try:
                self._category.find('name').string = value
            except AttributeError:
                new_tag = self.data.new_tag('name')
                new_tag.string = value
                self._category.append(new_tag)

    @category.deleter
    def category(self):
        self._category.find('id').string = '-1'
        self._category.find('name').string = 'None'

    @property
    def trigger_checkin(self):
        return self._trigger_checkin.string

    @trigger_checkin.setter
    def trigger_checkin(self, value):
        value = value.lower()
        if value not in ['true', 'false']:
            raise ValueError
        else:
            self._trigger_checkin.string = value

    @property
    def trigger_enrollment_complete(self):
        return self._trigger_checkin.string

    @trigger_enrollment_complete.setter
    def trigger_enrollment_complete(self, value):
        value = value.lower()
        if value not in ['true', 'false']:
            raise ValueError
        else:
            self._trigger_enrollment_complete.string = value

    @property
    def trigger_login(self):
        return self._trigger_login.string

    @trigger_login.setter
    def trigger_login(self, value):
        value = value.lower()
        if value not in ['true', 'false']:
            raise ValueError
        else:
            self._trigger_login.string = value

    @property
    def trigger_logout(self):
        return self._trigger_logout.string

    @trigger_logout.setter
    def trigger_logout(self, value):
        value = value.lower()
        if value not in ['true', 'false']:
            raise ValueError
        else:
            self._trigger_logout.string = value

    @property
    def trigger_network_state_changed(self):
        return self._trigger_network_state_changed.string

    @trigger_network_state_changed.setter
    def trigger_network_state_changed(self, value):
        value = value.lower()
        if value not in ['true', 'false']:
            raise ValueError
        else:
            self._trigger_network_state_changed.string = value

    @property
    def trigger_startup(self):
        return self._trigger_startup.string

    @trigger_startup.setter
    def trigger_startup(self, value):
        value = value.lower()
        if value not in ['true', 'false']:
            raise ValueError
        else:
            self._trigger_startup.string = value

    @property
    def trigger_other(self):
        return self._trigger_other.string

    @trigger_other.setter
    def trigger_other(self, value):
        self._trigger_other.string = value

    @trigger_other.deleter
    def trigger_other(self, value):
        del self._trigger_other

    @property
    def offline(self):
        return self._offline.string

    @offline.setter
    def offline(self, value):
        value = value.lower()
        if value not in ['true', 'false']:
            raise ValueError
        else:
            self._offline.string = value

    @property
    def frequency(self):
        return self._frequency.string

    @frequency.setter
    def frequency(self, value):
        if value not in ['Once per computer', 'Once per user per computer', 'Once per user', 'Once every day', 'Once every week', 'Once every month', 'Ongoing']:
            raise ValueError
        else:
            self._frequency.string = value

    @property
    def target_drive(self):
        return self._target_drive.string

    @target_drive.setter
    def target_drive(self, value):
        self._target_drive.string = value

    @property
    def site(self):
        return self._site

    @site.setter
    def site(self, value):
        if type(value) == int:
            print('test')
            self._site.find('id').string = str(value)
            self._site.find('name').decompose()
        elif type(value) == str:
            try:
                self._site.find('name').string = value
            except AttributeError:
                new_tag = self.data.new_tag('name')
                new_tag.string = value
                self._site.append(new_tag)

    @site.deleter
    def site(self):
        self._site.find('id').string = '-1'
        self._site.find('name').string = 'None'

    @property
    def update_inventory(self):
        return self._update_inventory.string

    @update_inventory.setter
    def update_inventory(self, value):
        value = value.lower()
        if value not in ['true', 'false']:
            raise ValueError
        else:
            self._update_inventory.string = value

    @property
    def reset_computer_name(self):
        return self._reset_computer_name.string

    @reset_computer_name.setter
    def reset_computer_name(self, value):
        value = value.lower()
        if value not in ['true', 'false']:
            raise ValueError
        else:
            self._reset_computer_name.string = value

    @property
    def install_cached_packages(self):
        return self._install_cached_packages.string

    @install_cached_packages.setter
    def install_cached_packages(self, value):
        value = value.lower()
        if value not in ['true', 'false']:
            raise ValueError
        else:
            self._install_cached_packages.string = value

    @property
    def fix_permissions(self):
        return self._fix_permissions.string

    @fix_permissions.setter
    def fix_permissions(self, value):
        value = value.lower()
        if value not in ['true', 'false']:
            raise ValueError
        else:
            self._fix_permissions.string = value

    @property
    def fix_by_host(self):
        return self._fix_by_host.string

    @fix_by_host.setter
    def fix_by_host(self, value):
        value = value.lower()
        if value not in ['true', 'false']:
            raise ValueError
        else:
            self._fix_by_host.string = value

    @property
    def fix_system_caches(self):
        return self._fix_system_caches.string

    @fix_system_caches.setter
    def fix_system_caches(self, value):
        value = value.lower()
        if value not in ['true', 'false']:
            raise ValueError
        else:
            self._fix_system_caches.string = value

    @property
    def fix_user_caches(self):
        return self._fix_user_caches.string

    @fix_user_caches.setter
    def fix_user_caches(self, value):
        value = value.lower()
        if value not in ['true', 'false']:
            raise ValueError
        else:
            self._fix_user_caches.string = value

    @property
    def verify_disk(self):
        return self._verify_disk.string

    @verify_disk.setter
    def verify_disk(self, value):
        value = value.lower()
        if value not in ['true', 'false']:
            raise ValueError
        else:
            self._verify_disk.string = value

    @property
    def search_by_path(self):
        return self._search_by_path.string

    @search_by_path.setter
    def search_by_path(self, value):
        self._search_by_path.string = value

    @property
    def delete_file(self):
        return self._delete_file.string

    @delete_file.setter
    def delete_file(self, value):
        value = value.lower()
        if value not in ['true', 'false']:
            raise ValueError
        else:
            self._delete_file.string = value

    @property
    def search_by_filename(self):
        return self._search_by_filename.string

    @search_by_filename.setter
    def search_by_filename(self, value):
        self._search_by_filename.string = value

    @property
    def update_locate_database(self):
        return self._update_locate_database.string

    @update_locate_database.setter
    def update_locate_database(self, value):
        value = value.lower()
        if value not in ['true', 'false']:
            raise ValueError
        else:
            self._update_locate_database.string = value

    @property
    def search_spotlight(self):
        return self._search_spotlight.string

    @search_spotlight.setter
    def search_spotlight(self, value):
        self._search_spotlight.string = value

    @property
    def search_process(self):
        return self._search_process.string

    @search_process.setter
    def search_process(self, value):
        self._search_process.string = value

    @property
    def kill_process(self):
        return self._kill_process.string

    @kill_process.setter
    def kill_process(self, value):
        value = value.lower()
        if value not in ['true', 'false']:
            raise ValueError
        else:
            self._kill_process.string = value

    @property
    def run_command(self):
        return self._run_command.string

    @run_command.setter
    def run_command(self, value):
        self._run_command.string = value

    def _create_tag(self, tag_name, arg):
        new_data_type = self.data.new_tag(tag_name)
        if type(arg) == int:
            new_sub_tag = self.data.new_tag('id')
        elif type(arg) == str:
            new_sub_tag = self.data.new_tag('name')
        new_sub_tag.string = str(arg)
        new_data_type.append(new_sub_tag)
        return new_data_type

    def _create_secondary_tag(self, tag_name, secondary_tag, secondary_arg, item):
        new_data_type = self.data.new_tag(tag_name)
        new_secondary_tag = self.data.new_tag(secondary_tag)
        if type(item) == int:
            new_sub_tag = self.data.new_tag('id')
        elif type(item) == str:
            new_sub_tag = self.data.new_tag('name')
        new_sub_tag.string = str(item)
        new_secondary_tag.string = str(secondary_arg)
        new_data_type.append(new_sub_tag)
        new_data_type.append(new_secondary_tag)
        return new_data_type

    def addComputers(self, *computers):
        arg_tuple = tuple(filter(lambda x: not self.computers.find(string=x), computers))
        tuple(map(lambda x: self.computers.append(self._create_tag('computer', x)), arg_tuple))

    def removeComputers(self, *computers):
        tuple(map(lambda x: self.computers.find(string=x).find_parent('computer').decompose(), computers))

    def addComputersGroups(self, *computersgroups):
        arg_tuple = tuple(filter(lambda x: not self.computergroups.find(string=x), computersgroups))
        tuple(map(lambda x: self.computergroups.append(self._create_tag('computer_group', x)), arg_tuple))

    def removeComputersGroups(self, *computersgroups):
        tuple(map(lambda x: self.computergroups.find(string=x).find_parent('computer_group').decompose(), computersgroups))

    def addBuildings(self, *buildings):
        arg_tuple = tuple(filter(lambda x: not self.buildings.find(string=x), buildings))
        tuple(map(lambda x: self.buildings.append(self._create_tag('building', x)), arg_tuple))

    def removeBuildings(self, *buildings):
        tuple(map(lambda x: self.buildings.find(string=x).find_parent('building').decompose(), buildings))

    def addDepartments(self, *departments):
        arg_tuple = tuple(filter(lambda x: not self.departments.find(string=x), departments))
        tuple(map(lambda x: self.departments.append(self._create_tag('department', x)), arg_tuple))

    def removeDepartments(self, *departments):
        tuple(map(lambda x: self.buildings.find(string=x).find_parent('department').decompose(), departments))

    def excludeComputers(self, *computers):
        arg_tuple = tuple(filter(lambda x: not self.exclusions.computers.find(string=x), computers))
        tuple(map(lambda x: self.exclusions.computers.append(self._create_tag('computer', x)), arg_tuple))

    def removeExcludedComputers(self, *computers):
        tuple(map(lambda x: self.exclusions.computers.find(string=x).find_parent('computer').decompose(), computers))

    def excludeComputersGroups(self, *computersgroups):
        arg_tuple = tuple(filter(lambda x: not self.exclusions.computergroups.find(string=x), computersgroups))
        tuple(map(lambda x: self.exclusions.computergroups.append(self._create_tag('computer_group', x)), arg_tuple))

    def removeExcludedComputersGroups(self, *computersgroups):
        tuple(map(lambda x: self.exclusions.computergroups.find(string=x).find_parent('computer_group').decompose(), computersgroups))

    def excludeBuildings(self, *buildings):
        arg_tuple = tuple(filter(lambda x: not self.exclusions.buildings.find(string=x), buildings))
        tuple(map(lambda x: self.exclusions.buildings.append(self._create_tag('building', x)), arg_tuple))

    def removeExcludedBuildings(self, *buildings):
        tuple(map(lambda x: self.exclusions.buildings.find(string=x).find_parent('building').decompose(), buildings))

    def excludeDepartments(self, *departments):
        arg_tuple = tuple(filter(lambda x: not self.exclusions.departments.find(string=x), departments))
        tuple(map(lambda x: self.exclusions.departments.append(self._create_tag('department', x)), arg_tuple))

    def removeExcludedDepartments(self, *args):
        tuple(map(lambda x: self.exclusions.departments.find(string=x).find_parent('department').decompose(), args))

    # def clear_scope(self):
    #     #To correct
    #     self.data.scope.clear()
    #     default_scope = soup(default_scope_template, 'xml')
    #     self.data.scope.append(default_scope)

    def addScripts(self, script=None, priority=None):
        # [ self.scripts.append(self._create_secondary_tag( 'script', 'priority', x,y)) for x, y in scripts.items() ]
        self.scripts.append(self._create_secondary_tag('script', 'priority', script, priority))

    def removeScripts(self, *scripts):
        tuple(map(lambda x: self.scripts.find(string=x).find_parent('script').decompose(), scripts))

    def addPackages(self, package=None, action=None):
        # [ self.packages.append(self._create_secondary_tag( 'package', 'action', x,y)) for x, y in packages.items() ]
        self.packages.append(self._create_secondary_tag('package', 'action', package, action))

    def removePackages(self, *packages):
        tuple(map(lambda x: self.scripts.find(string=x).find_parent('package').decompose(), packages))

    def mapPrinters(self, *printers):
        arg_tuple = tuple(filter(lambda x: not self.printers.find(string=x), printers))
        tuple(map(lambda x: self.printers.append(self._create_secondary_tag('printer', 'action', 'install', x)), arg_tuple))

    def unmapPrinters(self, *printers):
        arg_tuple = tuple(filter(lambda x: not self.printers.find(string=x), printers))
        tuple(map(lambda x: self.printers.append(self._create_secondary_tag('printer', 'action', 'uninstall', x)), arg_tuple))

    def removePrinters(self, *printers):
        tuple(map(lambda x: self.printers.find(string=x).find_parent('printer').decompose(), printers))

    def addBinding(self, *bindings):
        arg_tuple = tuple(filter(lambda x: not self.bindings.find(string=x), bindings))
        tuple(map(lambda x: self.bindings.append(self._create_tag('binding', x)), arg_tuple))

    def removeBindings(self, *bindings):
        tuple(map(lambda x: self.bindings.find(string=x).find_parent('binding').decompose(), bindings))

    def update(self):
        return Policies.putById(str(self.id), str(self.data))

    def delete(self):
        return Policies.deleteById(str(self.id))


class Printers():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')


class RemovableMacAddresses():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')


class RestrictedSoftware():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')


class Scripts():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')


class Sites():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')


class SmtpServer():

    @classmethod
    def get(cls):
        '''Return list of accounts'''
        return get_call(__class__.__name__.lower())

    @classmethod
    def put(cls, server):
        ''''''
        return put_call(__class__.__name__.lower(), server)


class SoftwareUpdateServers():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')


class UserExtensionAttributes():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')


class UserGroups():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')


class Users():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def getByEmail(cls, email):
        return get_call(f'{__class__.__name__.lower()}/email/{email}')


class VppAccounts():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')


class VppAssignments():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')


class VppInvitations():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getSubset(cls, item, subset_items):
        return get_call(f'{__class__.__name__.lower()}/id/{item}/subset/{subset_items}')


class Webhooks():

    @classmethod
    def get(cls):
        return get_call(__class__.__name__.lower())

    @classmethod
    def getById(cls, id_item):
        return get_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def putById(cls, id_item, data):
        return put_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def postById(cls, id_item, data):
        return post_call(f'{__class__.__name__.lower()}/id/{id_item}', data)

    @classmethod
    def deleteById(cls, id_item):
        return delete_call(f'{__class__.__name__.lower()}/id/{id_item}')

    @classmethod
    def getByName(cls, name_item):
        return get_call(f'{__class__.__name__.lower()}/name/{name_item}')

    @classmethod
    def putByName(cls, name_item, data):
        return put_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def postByName(cls, name_item, data):
        return post_call(f'{__class__.__name__.lower()}/name/{name_item}', data)

    @classmethod
    def deleteByName(cls, name_item):
        return delete_call(f'{__class__.__name__.lower()}/name/{name_item}')
